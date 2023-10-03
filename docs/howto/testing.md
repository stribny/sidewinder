# Testing

Sidewinder comes with a small test suite that provides examples for writing unit tests, API tests, and UI tests.

## Run tests

By default, pytest is configured to run tests without end-to-end UI tests:

```bash
# inside project root
poetry shell

# inside virtual environment
pytest
```

## Run UI tests

```bash
pytest -m ui
```
