# OpenFisca Aotearoa (Active Mainline)

> [!NOTE]
> This repository (`edithatogo/openfisca-aotearoa`) is the **definitive active mainline fork** of the New Zealand OpenFisca rules package. The legacy repositories hosted at `BetterRules/openfisca-aotearoa` and `digitalaotearoa/openfisca-aotearoa` are treated by this project as dormant upstream references; they may still appear as public, unarchived GitHub repositories.
> This fork is being modernized around Python 3.11+, UV-compatible dependency management, Ruff linting, a basic Basedpyright baseline, Polars integrations, and automated legislative drafting agents.

The OpenFisca Aotearoa project is an Open Source project dedicated to providing computational models of New Zealand's legislation, regulation, and government policy. 

It is a New Zealand specific Rules-as-Code project implemented in [OpenFisca](https://openfisca.org). 

> The codebase was originally started in 2018 within the "Service Innovation Lab", a New Zealand government initative that was tasked with looking at whole-of-government approaches to service innovation. The Lab was hosted within the Department of Internal Affairs (DIA) as no "whole of government" entity existed. The work included service design approaches based on life events such as the birth of a child and the idea that one service could avoid parents having to contact multiple government departments (see https://smartstart.services.govt.nz/). The Lab's eventual closure came about due to internal DIA funding priorities.

This project was continued initially by former members of the Lab and the code base, contributors and uses have widened through a number of citizen led initiatives.


## Minimal Installation - for users running the rules

This section will be available again in the near term, once a stable release strategy has been reimplemented which will see the resumption of releases on [PyPI](https://pypi.org/).

## Install Instructions for Users and Contributors

This package requires Python 3.11+. These installation instructions assume python is installed and accessible via the command line.

All platforms that can execute Python are supported, which includes GNU/Linux, macOS and Microsoft Windows.

We use **UV Workspaces** to manage the project environment and dependencies.
See [UV and una workspace commands](docs/workspace.md) for the full standalone
and parent-repository command set.

### Clone the repository

Via the terminal, clone the repository and `cd openfisca-aotearoa` into the project directory.

### Environment Setup with UV
```sh
# Sync the workspace and install all dependencies
uv sync
```

### Testing

To run the full OpenFisca Aotearoa test suite:
```sh
uv run pytest
```

## Web API

To serve an instance of the OpenFisca Aotearoa web API:
```sh
uv run openfisca serve
```

You can make sure that your instance of the API is working by requesting:
```sh
curl "http://localhost:5000/spec"
```

To read more about the `openfisca serve` command, check out its [documentation](https://openfisca.readthedocs.io/en/latest/openfisca_serve.html).

## Alternatives

- [Run OpenFisca Aotearoa in vscode with devcontainer](docs/devcontainer.md). Creates a development environment in Visual Studio Code using the VSCode Development container approach. Requires Docker.

- [Setup your virtual environment with pyenv](docs/pyenv.md)

- [Build a docker image and run the OpenFisca web API with it](docs/docker.md)


## Next Steps

- To write new legislation, read [this repository's wiki](https://github.com/edithatogo/openfisca-aotearoa/wiki) along with the OpenFisca [Coding the legislation](https://openfisca.org/doc/coding-the-legislation/index.html) section.
- To contribute to the code, read our [contribution doc](https://github.com/edithatogo/openfisca-aotearoa/blob/main/CONTRIBUTING.md).
