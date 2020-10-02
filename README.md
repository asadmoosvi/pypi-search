# pypi-search

pypi-search allows you to quickly query packages on PyPI.
It fetches the following information:
- Version Information
- Project Links
- Github Stats if any
- Meta Information (author, maintainer)
- Description

It quickly allows you to know what a package is all about without having to open up
the PyPI website.

# usage

In order to use the package you need to run the `main.py` as a module. So after
going into the top level directory of this repo, you can run `python -m pypi_search.main query` where
`query` is the package you want the information for. By default it doesn't fetch the long
description for the package. In order to fetch that you can use the `-d` flag.

## help menu

```
usage: main.py [-h] [-d] search

Search for PyPi packages

positional arguments:
  search             Package to show information on

optional arguments:
  -h, --help         show this help message and exit
  -d, --description  Show package description
```


# todo

In order to make this easier to use I will be making a package out of this
so it can easily be installed via `pip`.
