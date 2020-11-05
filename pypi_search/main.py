from pypi_search.utils import PyPiPage
from pypi_search.arg_parser import parse_args
from pypi_search.log import init_logger
from pypi_search.search import find_packages
from typing import Optional, Sequence
import sys, os
import webbrowser


logger = init_logger(__name__)


def main(argv: Optional[Sequence[str]] = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    args = parse_args(argv)

    logger.info(f'Searching for package `{args.search}`...')
    pypi = PyPiPage(args.search)
    if not pypi.found():
        logger.info(f'Could not find package `{args.search}`')
        logger.info('Searching for other packages that match that query...')
        packages_found = find_packages(args.search)
        if packages_found:
            print(f'\nHere are some packages that match `{args.search}`:')
            print('=' * os.get_terminal_size().columns + '\n')
            for pkg in packages_found:
                print(f"Name         : {pkg['name']}")
                print(f"Version      : {pkg['version']}")
                print(f"Release date : {pkg['release_date']}")
                print(f"Description  : {pkg['description']}\n")
        else:
            logger.info('No packages found')
        return 1

    version_info = pypi.get_version_info()
    project_links = pypi.get_project_links()
    github_stats = pypi.get_github_stats()
    meta_info = pypi.get_meta_info()

    summary = pypi.get_project_description_summary()
    homepage_url = None
    print(f'\n{args.search.lower()}:')
    print(f'    - {summary}')
    print('\nVersion Information:')
    print(f"    - version number: {version_info['version_no']}")
    print(f"    - release date  : {version_info['release_date']}")
    print("Project Links:")
    for link_name, link in project_links.items():
        print(f"    - {link_name}: {link}")
        if link_name == 'Homepage':
            homepage_url = link
    if github_stats:
        print("Github Stats:")
        for key, val in github_stats.items():
            print(f"    - {key}: {val}")
    print("Meta Information:")
    for key, val in meta_info.items():
        if key == 'author':
            val = (
                f"\n        name: {val['name']}"
                f"\n        email: {val['email']}"
            )
        print(f"    - {key}: {val}")

    if args.description:
        print()
        print('=' * os.get_terminal_size().columns + '\n')
        print(pypi.get_project_description())

    if args.open:
        print()
        if homepage_url:
            logger.info(f"Opening homepage `{homepage_url}` in default browser.")
            webbrowser.open(homepage_url)
        else:
            logger.info("No homepage available.")


    return 0

if __name__ == '__main__':
    exit(main())
