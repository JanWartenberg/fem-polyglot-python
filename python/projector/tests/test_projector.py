"""
from root call:

python -m tests.test_projector """
import unittest

from config import Config, Operation
from projector import Data, Projector


def create_data() -> Data:
    return {
        "projector": {
            "D:\\":
            {"foo": "bar1",
             "fem": "is_great"
             },
            r"D:\tmp":
            {"foo": "bar2"},
            r"D:\tmp\foo":
            {"foo": "bar3"},
        }}


def get_projector(pwd: str, data: Data = None) -> Projector:
    cfg = Config.from_dict({
        "args": [],
        "operation": Operation.print,
        "pwd": pwd,
        "config": "whatever"
    })
    if data is None:
        data = create_data()
    return Projector(cfg, data)


class ProjectorTest(unittest.TestCase):
    def test_get_value_all(self):
        proj = get_projector(r"D:\tmp\foo")
        ret = proj.get_value_all()
        self.assertEqual(ret, {"fem": "is_great", "foo": "bar3"})

    def test_get_value(self):
        proj = get_projector(r"D:\tmp\foo")
        ret = proj.get_value("foo")
        self.assertEqual(ret, "bar3")

        proj = get_projector(r"D:\tmp")
        ret = proj.get_value("foo")
        self.assertEqual(ret, "bar2")

        proj = get_projector("D:\\")
        ret = proj.get_value("fem")
        self.assertEqual(ret, "is_great")

    def test_set_value(self):
        proj = get_projector(r"D:\tmp\foo")
        proj.set_value("foo", "baz")

        self.assertEqual(proj.get_value("foo"), "baz")

        proj.set_value("fem", "is_better_than_great")
        self.assertEqual(proj.get_value("fem"), "is_better_than_great")

        proj2 = get_projector("D:\\", proj.data)
        self.assertEqual(proj2.get_value("fem"), "is_great")

    def test_remove_value(self):
        proj = get_projector(r"D:\tmp\foo")
        proj.remove_value("fem")
        self.assertEqual(proj.get_value("fem"), "is_great")
        proj.remove_value("foo")
        self.assertEqual(proj.get_value("foo"), "bar2")


if __name__ == "__main__":
    unittest.main()
