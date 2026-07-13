# Justfile for Nightingale CLI
# Use `just <recipe>` to run commands

# Default recipe - show available commands
default:
    @just --list

# Install dependencies using UV
install:
    uv pip install -e .

# Install development dependencies
install-dev:
    uv pip install -e ".[dev]"

# Run the CLI with a sample input
run INPUT:
    uv run python -m nightingale.cli {{INPUT}}

# Run the CLI with verbose output
run-verbose INPUT:
    uv run python -m nightingale.cli {{INPUT}} --verbose

# Format code with black
format:
    uv run black nightingale/

# Lint code with ruff
lint:
    uv run ruff check nightingale/

# Lint and fix issues
lint-fix:
    uv run ruff check --fix nightingale/

# Type check with mypy
typecheck:
    uv run mypy nightingale/

# Run all quality checks (format, lint, typecheck)
check:
    @echo "Running code quality checks..."
    just format
    just lint
    just typecheck

# Run tests with pytest
test:
    uv run pytest

# Run tests with coverage
test-cov:
    uv run pytest --cov=nightingale --cov-report=html --cov-report=term

# Clean build artifacts and cache
clean:
    rm -rf build/
    rm -rf dist/
    rm -rf *.egg-info
    rm -rf .pytest_cache/
    rm -rf .coverage
    rm -rf htmlcov/
    rm -rf .mypy_cache/
    rm -rf .ruff_cache/
    find . -type d -name __pycache__ -exec rm -rf {} +

# Build the package
build:
    uv build

# Create a new virtual environment with UV
venv:
    uv venv

# Sync dependencies with UV
sync:
    uv pip sync

# Show project info
info:
    @echo "Nightingale - GitHub Issue Prioritizer"
    @echo "======================================"
    @echo "Python version: $(python --version)"
    @echo "UV version: $(uv --version)"
    @echo ""
    @echo "Available commands:"
    @just --list
