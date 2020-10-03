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

# installation

To get the latest stable release from PyPI:
- `pip install pypi-search`

To get the latest dev release, go into the root of this project and run:
- `pip install .`

# usage

[![asciicast](https://asciinema.org/a/JTlNXr0PrfDT9exEDkGQeklGz.svg)](https://asciinema.org/a/JTlNXr0PrfDT9exEDkGQeklGz)

get information on a package called `foo`:
---
`pypisearch foo`

get information on a package called `foo` along with its long description:
---
`pypisearch -d foo`

## help menu

```
usage: pypisearch [-h] [-d] search

Search for PyPi packages

positional arguments:
  search             Package to show information on

optional arguments:
  -h, --help         show this help message and exit
  -d, --description  Show package description
```


# todo

- [x] In order to make this easier to use I will be making a package out of this
so it can easily be installed via `pip`.
