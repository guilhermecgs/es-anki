# Python Package Management Rule

Use `uv` as the default and mandatory package manager for all Python tasks in this repository.

## Always use `uv`

- Install dependencies with `uv add <package>`.
- Remove dependencies with `uv remove <package>`.
- Run Python scripts with `uv run <command>`.
- Sync dependencies with `uv sync`.
- Prefer `uv pip` over `pip` when direct pip-compatible commands are required.

## Avoid

- Do not use `pip install`, `pip uninstall`, `poetry`, or `pipenv`.
- Do not suggest alternative Python package managers unless explicitly requested by the user.
