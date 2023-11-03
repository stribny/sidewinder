# Installation

!!! info

    Sidewinder is set up as a template on GitHub which means you can easily create your own GitHub repository by clicking on the big green "Use this template" button on the repository homepage. This will ensure you have your own clean repository without previous commits and without any link to the original project.

## Clone the project locally

After you create your own GitHub repository from template or by [forking the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo), clone it locally from your repository URL.

Alternatively just clone the project directly from the main repo:

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

If you plan to use this feature, install dependencies in the next step with `--with graphviz`.

You can also skip this step if you don't plan to use this feature. 

## Install Sidewinder

You can now install Sidewinder from the project's root:

```bash
poetry install

# or with mkdocs

poetry install --with docs

# or with graphviz

poetry install --with graphviz

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

Now, [configure the project](configuration.md).