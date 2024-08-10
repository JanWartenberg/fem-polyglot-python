import json
import os
from typing import Dict, List, Optional, TypedDict

from config import Config


class Data(TypedDict):
    """
    projectorData = {
            # pwd
            [key: str]: {
                # key      -> value
                [key: str]: str,
                }
            }
    """
    projector: List[Dict[str, str]]


defaultData: Data = {"projector": {}}


class Projector:
    def __init__(self, config: Config, data: Data):
        self.config = config
        self.data = data

#    def from_config(config: Config) -> Projector:
    def from_config(config: Config):
        # an error will produce a default config
        if os.path.exists(config.config):
            try:
                with open(config.config, "r") as fp:
                    data = json.load(fp)
            except json.JSONDecodeError:
                data = defaultData
            return Projector(config, data)
        else:
            return Projector(config, defaultData)

    def get_value_all(self) -> Dict[str, str]:
        curr = self.config.pwd
        prev = ""
        paths = []

        while (curr != prev):
            prev = curr
            paths.append(curr)
            curr = os.path.dirname(curr)

        paths.reverse()

        res = {}
        for path in paths:
            value = self.data["projector"].get(path)
            if value:
                res.update(value)
        return res

    def get_value(self, key: str) -> Optional[str]:
        curr = self.config.pwd
        prev = ""
        out = None

        while (curr != prev):
            value = self.data["projector"].get(curr, {}).get(key)
            if value:
                out = value
                break
            prev = curr
            curr = os.path.dirname(curr)
        return out

    def set_value(self, key: str, value: str) -> None:
        dir = self.data["projector"].get(self.config.pwd)
        if not dir:
            dir = self.data["projector"][self.config.pwd] = {}
        dir[key] = value

    def remove_value(self, key: str) -> None:
        dir = self.data["projector"][self.config.pwd]
        if dir:
            if key in dir:
                del dir[key]

    def save(self):
        config_path = os.path.dirname(self.config.config)
        if os.path.exists(config_path):
            os.makedirs(config_path, exist_ok=True)
        with open(self.config.config, "w") as f:
            json.dump(self.data, f)


