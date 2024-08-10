"""
Run unittest from project dir:
    python -m tests.test_config
"""
import unittest

from config import Config, Operation, InputError
# Since we did not adhere to Primeagen's example with the get_config
# and chucked everything into a class, we already need a second import
# for this simple test example"""
from opts import get_projector_options


class ConfigTest(unittest.TestCase):
    def test_print_all(self):
        config = Config(get_projector_options())

        self.assertEqual(config.operation, Operation.print)
        self.assertEqual(config.args, [])

    def test_print_key(self):
        config = Config(get_projector_options(args=["foo"]))

        self.assertEqual(config.operation, Operation.print)
        self.assertEqual(config.args, ["foo"])

    def test_explicit_print_key(self):
        config = Config(get_projector_options(args=["print", "foo"]))

        self.assertEqual(config.operation, Operation.print)
        self.assertEqual(config.args, ["foo"])

    def test_add_key(self):
        config = Config(get_projector_options(args=["add", "foo", "bar"]))

        self.assertEqual(config.operation, Operation.add)
        self.assertEqual(config.args, ["foo", "bar"])

    def test_add_key_but_fail(self):
        opts = get_projector_options(args=["add", "foo"])

        with self.assertRaises(InputError):
            Config(opts)

    def test_remove_key(self):
        config = Config(get_projector_options(args=["rm", "foo"]))

        self.assertEqual(config.operation, Operation.remove)
        self.assertEqual(config.args, ["foo"])

    def test_remove_key_but_fail(self):
        opts = get_projector_options(args=["rm", "foo", "bar"])

        with self.assertRaises(InputError):
            Config(opts)


if __name__ == "__main__":
    unittest.main()
