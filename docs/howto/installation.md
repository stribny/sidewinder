# Installation

!!! info

    Sidewinder is set up as a template on GitHub which means you can easily create your own GitHub repository by clicking on the big green "Use this template" button on the repository homepage. This will ensure you have your own clean repository without previous commits and without any link to the original project.

## Clone the project locally

After you create your own GitHub repository from template or by [forking the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo), clone it locally from your repository URL.

Alternatively just clone the project directly from the main repo:

```bash
git clone https://github.com/stribny/sidewinder
```

## Prerequisites

Before installing Sidewinder, you will need the dependency manager [uv](https://docs.astral.sh/uv/) to be installed in order to invoke the `uv` command.

## Installing developer tooling

`uv` will automatically install all dependencies when `uv run` is executed. However, some development
dependencies require specific installation instructions.

Run the following commands in the project's root directory:

```bash
# Install pre-commit hooks
uv run -- pre-commit install

# Install Playwright

uv run -- playwright install
```

Now, [configure the project](configuration.md).
