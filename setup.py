import setuptools


with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as req_f:
    install_requires=req_f.read().split()

setuptools.setup(
    name="pypi-search",
    version="1.0.0",
    author="Asad Moosvi",
    author_email="moosvi.asad@gmail.com",
    description="Get Information on Python Packages From PyPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asadmoosvi/pypi-search",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    python_requires=">=3.6",
    install_requires=install_requires,
    entry_points= {
        "console_scripts": ["pypisearch=pypi_search.main:main"]
    }
)
