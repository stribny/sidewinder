# Testing

Sidewinder comes with a small test suite that provides examples for writing unit tests, HTTP API tests, and UI tests.

## Run tests

By default, pytest is configured to run tests without end-to-end UI tests:

```bash
uv run -- pytest
```

## Run UI tests

```bash
uv run -- pytest -m ui
```
