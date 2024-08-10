"""This module just parses the CLI args into an Options "Namespace"."""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("args", nargs="*")
parser.add_argument("-c", "--config")
parser.add_argument("-p", "--pwd")


def get_projector_options(**kwargs):
    return parser.parse_args(**kwargs)
