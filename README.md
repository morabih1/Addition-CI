# Python Calculator

![Calculator CI](https://github.com/morabih1/Addition-CI/actions/workflows/ci.yml/badge.svg)

A simple command-line calculator built for the CSCI313 Software Engineering project (Phase 1).

## Features

- A `Calculator` class with `add()`, `subtract()`, `multiply()` and `divide()`
- Type a full expression such as `2 + 3`, `10 / 4`, or `6 * 7`
- Supports `+`, `-`, `*`, and `/`; invalid expressions and division by zero show clear errors
- Keeps running until you choose **q** to quit
- Unit tests for every operation and expression input, run automatically by GitHub Actions

## Requirements

Python 3.10 or newer. No extra packages are needed.

## Run the calculator

```bash
python calculator.py
```

Example session:

```
=== Simple Calculator ===

Enter expression (or q to quit): 2 + 3
Result: 2 + 3 = 5
Enter expression (or q to quit): q
Goodbye!
```

## Run the tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

| Path | What it contains |
| --- | --- |
| `calculator.py` | The `Calculator` class and expression-based command line |
| `tests/test_add.py` | Tests for `add` |
| `tests/test_subtract.py` | Tests for `subtract` |
| `tests/test_multiply.py` | Tests for `multiply` |
| `tests/test_divide.py` | Tests for `divide`, including divide by zero |
| `tests/test_cli.py` | Scenario tests for expression input (system / use-case testing) |
| `.github/workflows/ci.yml` | GitHub Actions workflow that runs all tests |

## Continuous integration

Every push and every pull request triggers the **Calculator CI** workflow (`.github/workflows/ci.yml`). It has two jobs:

1. **test** sets up Python 3.12 and runs all unit tests.
2. **demo** runs only if `test` passes, and runs the calculator with sample input to show it works end to end.

Because all tests run again on every change, this also acts as regression testing. A pull request should only be merged when both jobs are green.

## Team workflow

1. Pick an issue from the project board and move it to **In Progress**.
2. Create a branch for it: `feature/<short-name>` for new features (e.g. `feature/multiply`), `bugfix/<short-name>` for bugs (e.g. `bugfix/divide-by-zero`).
3. Make small commits with clear messages, then open a pull request with a clear title and `Closes #<issue number>` in the description.
4. A teammate reviews the PR. Merge after approval and a green CI run, then move the card to **Done**.
