# UV Package Manager Migration

This project has been refactored to use the [uv](https://github.com/astral-sh/uv) package manager for faster, more reliable Python package management.

## What Changed

### New Files
- **`pyproject.toml`**: Modern Python project configuration file following PEP 621 standards
  - Contains all project metadata previously in `setup.py`
  - Defines dependencies and optional dependencies (dev tools)
  - Configures the `nightingale` CLI entry point
  
- **`.python-version`**: Specifies the Python version for uv to use (3.12)

### Updated Files
- **`.github/workflows/python-package.yml`**: CI/CD workflow now uses uv instead of pip
- **`README.md`**: Added installation instructions for uv
- **`.gitignore`**: Updated to track `.python-version` and ignore uv cache files

### Preserved Files
- **`setup.py`**: Kept for backward compatibility
- **`requirements.txt`**: Kept for backward compatibility (though pyproject.toml is now the source of truth)

## Benefits of UV

1. **Speed**: UV is 10-100x faster than pip for package installation
2. **Reliability**: Better dependency resolution and reproducible builds
3. **Modern**: Uses the standard `pyproject.toml` format (PEP 621)
4. **Compatible**: Works with existing pip-based workflows

## Development Workflow

### Setting up the development environment

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/kjgarza/nightingale.git
cd nightingale

# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in editable mode with dev dependencies
uv pip install -e ".[dev]"
```

### Running the CLI

```bash
# After installation, you can run the CLI directly
nightingale issues.csv

# Or via Python module
python -m nightingale.cli issues.csv
```

### Running linters

```bash
# Activate the virtual environment first
source .venv/bin/activate

# Run flake8
flake8 nightingale/ tests/ --count --max-complexity=10 --max-line-length=127
```

## Backward Compatibility

The project still supports traditional pip installation:

```bash
pip install -e .
```

All existing workflows and installation methods continue to work.
