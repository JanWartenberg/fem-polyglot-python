"""this module manages the config,
i.e. the collection of what to do (operation), with which params (args),
config (path to the config), and present working dir (pwd) """
from enum import Enum, auto
import os
from pathlib import Path

from opts import get_projector_options


class InputError(Exception):
    """Exception raised when some input is not in the expected format """

    def __init__(self, parameter_name):
        self.parameter_name = parameter_name
        self.message = f"Input Error: {parameter_name}"
        super().__init__(self.message)


class Operation(Enum):
    print = auto()
    add = auto()
    remove = auto()


class Config():
    args: str
    operation: Operation
    config: str  # string path to the item
    pwd: str

    def __init__(self,
                 opts: get_projector_options() = get_projector_options()):
        self.args = self._get_args(opts)
        self.operation = self._get_operation(opts)
        self.config = self._get_config(opts)
        self.pwd = self._get_pwd(opts)

    def from_dict(input_dict):
        # not ideal to create it first then overwrite
        # but best/quickest hack
        cfg = Config()
        cfg.args = input_dict["args"]
        cfg.operation = input_dict["operation"]
        cfg.pwd = input_dict["pwd"]
        cfg.config = input_dict["config"]
        return cfg

    def _get_pwd(self, opts):
        if opts.pwd:
            return opts.pwd
        return os.getcwd()

    def _get_config(self, opts):
        if opts.config:
            return opts.config
        if Path.home():
            home = Path.home()
            return os.path.join(home, ".projector.json")
        else:
            raise InputError("Path to config not found")

    def _get_operation(self, opts):
        if not opts.args or len(opts.args) == 0:
            return Operation.print

        if opts.args[0] == "add":
            return Operation.add

        if opts.args[0] == "rm":
            return Operation.remove

        if opts.args[0] == "print":
            del opts.args[0]
            return Operation.print

        return Operation.print

    def _get_args(self, opts):
        if not opts.args or len(opts.args) == 0:
            return []
        operation = self._get_operation(opts)
        if operation == Operation.print:
            if len(opts.args) > 1:
                raise InputError("Expected 0 or 1 arguments but got " +
                                 f"{len(opts.args)}")
            return opts.args

        if operation == Operation.add:
            if len(opts.args) != 3:
                raise InputError("Expected 2 arguments but got " +
                                 f"{len(opts.args)-1}")
            return opts.args[1:]

        if operation == Operation.remove:
            if len(opts.args) != 2:
                raise InputError("Expected 1 argument but got " +
                                 f"{len(opts.args)-1}")
            return opts.args[1:]

    def __str__(self):
        return f"{type(self).__name__}(args={self.args}, " +\
            f"operation={self.operation}, config={self.config}, " +\
            f"pwd={self.pwd})"
