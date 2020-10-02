import argparse
from typing import Sequence


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Search for PyPi packages')
    parser.add_argument('search', help='Package to show information on')
    parser.add_argument(
        '-d', '--description', help='Show package description',
        action='store_true'
    )
    args = parser.parse_args(argv)
    return args
