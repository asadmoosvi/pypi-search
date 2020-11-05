import argparse
from typing import Sequence
from pypi_search import __version__


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Search for PyPi packages')
    parser.add_argument('search', help='Package to show information on')
    parser.add_argument(
        '-d', '--description', help='Show package description',
        action='store_true'
    )
    parser.add_argument(
        '--version', action='version',
        version=f'%(prog)s {__version__}'
    )
    parser.add_argument(
        '-o', '--open',
        action='store_true',
        help='Open homepage in browser'
    )
    args = parser.parse_args(argv)
    return args
