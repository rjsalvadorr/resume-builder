# resume-builder

A more structured approach to handling job search documents

## SETUP

This tool requires [pandoc](https://pandoc.org/installing.html).  
However, note the following from the [pandoc PyPI package](https://pypi.org/project/pandoc/):

> This documentation is dedicated to the [latest version of the project available on github](https://github.com/boisgera/pandoc). It is automatically tested with Python 3.12.4 against pandoc 3.2.1. At the moment I am writing this, [the latest release of pandoc for conda](https://anaconda.org/conda-forge/pandoc) is pandoc 3.2.1.

The tool attempts to run anyways with a more recent version installed:

> /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/pandoc/utils.py:62: UserWarning:  
Pandoc version 3.7.0.2 is not supported, we proceed as if pandoc 3.2.1 was used.  
The behavior of the library is undefined if the document models of these versions differ.  
warnings.warn(error)

## USAGE

1. Be in the root directory of this repo
1. Run `python3 src/build.py`
