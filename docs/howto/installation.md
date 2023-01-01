# Installation

!!! info

    There is currently no project generator. To start using Sidewinder, clone the [repository](https://github.com/stribny/sidewinder) and make configuration
    changes in your local copy.

## Clone the repository

!!! tip

    Feel free to [fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo) first so that you don't have to
    set up Git remotes later.

You can clone Sidewinder from the official repository or your fork:

```
git clone https://github.com/stribny/sidewinder
```

## Prerequisites

### Install Python 3.9+

Before installing Sidewinder, you will need Python 3.9 and [Poetry](https://python-poetry.org/) dependency manager.

### Install Poetry

You can install Poetry with `pip`:

```
pip install poetry
```

### Install watchman

For fast hot-reloading, make sure to install [watchman](https://facebook.github.io/watchman/docs/install.html).

### Install graphviz (optional)

Graphviz is needed by [django-extensions](https://django-extensions.readthedocs.io) for generating model diagrams. You will need to figure out how to
install it for your system. 

On Fedora, use `dnf`:

```
dnf install graphviz graphviz-devel
```

You can also skip this step if you don't plan to use this feature. To do so, ignore the `--all-extras` in the following step.

## Install Sidewinder

You can now install Sidewinder from the project's root:

```bash
poetry install --all-extras

# install pre-commit hooks
poetry run pre-commit install
```

From this point onwards, all commands should be run inside the created virtual environment. You can switch to the virtual environment with:

```
poetry shell
```

## Install Playwright

```bash
# inside virtual environment
playwright install
```

## Install Bulma

```
cd assets
npm i
npm run build-bulma
```

Now, [configure the project](configuration.md).