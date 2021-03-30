# Overview

Meddra toolkit to handle ontology files

This project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter) using [jacebrowning/template-python](https://github.com/jacebrowning/template-python).

# Setup

## Requirements

* Python 3.9+

## Installation

Add POSOS PyPi repository in your configuration.

Install `meddra-toolkit` into an activated virtual environment:

```text
$ pip install meddra-toolkit
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add meddra-toolkit
```

# Usage

After installation, the package can imported.
Then load a Meddra Version and explore it:

```python
from meddra_toolkit import meddra
base = meddra.MeddraData(meddra.VERSION_24_0_FR)
base.load()
result = base.find("covid", regex=True)
# `result` is an array of `MeddraConcept`

# A MeddraConcept has a `code`, a `name`, some `parents` and `children`
# and a concept_type() method that returns concept level in Meddra hierarchy
# PTs also have `soc` field pointing to the PT's preferred SOC
# LLTs has no parents but a `pt` field pointing to it's PT

# `find()` method takes a positional argument which is the term to find, that
# can be either a code or a name. If the `regex` flag is True, only the name
# of the concepts will be tested and the `term` string will be considered
# a case-insentitive regular expression.

# A MeddraData object has a `concepts` field which is a dictionnary of all
# concepts, where keys are meddra identifiers and values are the concept
# objects.
```

# Documentation

Run `make mkdocs-serve` to load documentation.