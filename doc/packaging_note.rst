Packaging and installation
==========================

This project supports modern Python packaging via `pyproject.toml` and
can be installed with `pip` as described in the top-level README.

Recommended commands:

    $ python -m pip install .
    $ python -m pip install -e .  # editable

The `debian/` directory contains legacy Debian packaging metadata and
is provided for archival / packaging reference only. Prefer the `pip`
workflow for development and distribution.
