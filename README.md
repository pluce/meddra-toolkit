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
```

# Documentation

Run `make mkdocs-serve` to load documentation.