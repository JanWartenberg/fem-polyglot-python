"""Example CLI app to handle config options (key+value).
Based on Primeagens "Polyglot" course of Frontendmasters,
where he implemented in it Typescript/Go/Rust."""
from opts import get_projector_options
from config import Config, Operation
from projector import Projector


def project():
    opts = get_projector_options()
    cfg = Config(opts)
    proj = Projector.from_config(cfg)

    if cfg.operation == Operation.print:
        if len(cfg.args) == 0:
            print(proj.get_value_all())
        else:
            val = proj.get_value(cfg.args[0])
            if val:
                print(val)

    if cfg.operation == Operation.add:
        proj.set_value(cfg.args[0], cfg.args[1])
        proj.save()

    if cfg.operation == Operation.remove:
        proj.remove_value(cfg.args[0])
        proj.save()


def main():
    project()


if __name__ == "__main__":
    main()
