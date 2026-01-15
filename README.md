# Nightingale 🐦 - GitHub Issue Prioritizer

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![GitHub issues](https://img.shields.io/github/issues/kjgarza/nightingale)](https://github.com/kjgarza/nightingale/issues)
[![GitHub stars](https://img.shields.io/github/stars/kjgarza/nightingale)](https://github.com/kjgarza/nightingale/stargazers)

A modern, interactive CLI tool that uses binary search comparison to prioritize GitHub issues. Built with best practices for Python CLI development, featuring rich terminal output and an intuitive user experience.

![](https://raw.githubusercontent.com/kjgarza/nightingale/master/nigthtingale_logo.png)

## Features

✨ **Interactive Binary Comparison** - Uses efficient binary insertion sort to minimize comparisons
🎨 **Rich Terminal UI** - Beautiful, colored output with tables and panels
📝 **Flexible Input** - Accepts CSV files or URLs to GitHub issue lists
💾 **File Export** - Save prioritized results to a file
🔍 **Verbose Logging** - Debug mode for detailed execution information
⚡ **Modern Python** - Built with Click, Rich, and UV package manager

## Prerequisites

- **Python 3.8+**
- **UV** package manager (recommended) or pip
- **Just** command runner (optional, for convenience)

### Installing Prerequisites

**UV (Fast Python package manager):**
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Just (Command runner):**
```bash
# macOS
brew install just

# Linux
cargo install just

# Or download from: https://github.com/casey/just
```

## Installation

### Using UV (Recommended)

```bash
# Clone the repository
git clone https://github.com/kjgarza/nightingale.git
cd nightingale

# Install with UV
uv pip install -e .

# Or use just
just install
```

### Using pip

```bash
# Clone the repository
git clone https://github.com/kjgarza/nightingale.git
cd nightingale

# Install
pip install -e .
```

### Development Installation

```bash
# Install with development dependencies
uv pip install -e ".[dev]"

# Or use just
just install-dev
```

## Usage

### Basic Usage

```bash
# From CSV file
nightingale issues.csv

# From URL
nightingale https://github.com/user/repo/issues

# With output file
nightingale issues.csv --output prioritized.txt

# With verbose logging
nightingale issues.csv --verbose
```

### Using Just Commands

```bash
# Run with a sample input
just run issues.csv

# Run with verbose output
just run-verbose issues.csv

# See all available commands
just --list
```

### Command-Line Options

```
Usage: nightingale [OPTIONS] INPUT

  Prioritize GitHub issues using interactive binary comparison.

Arguments:
  INPUT                Path to CSV file or URL to GitHub issue list

Options:
  -o, --output PATH    Output file path for prioritized issues
  -v, --verbose        Enable verbose output for debugging
  --version            Show version and exit
  -h, --help           Show this message and exit
```

### Example Session

```
$ nightingale issues.csv

╭─────────────────────────────────────────────────────╮
│  Nightingale - GitHub Issue Prioritizer            │
│  Interactive binary comparison for prioritization  │
╰─────────────────────────────────────────────────────╯

Which issue is more important?
1. Fix critical authentication bug #123
2. Update documentation for API #456
Enter your choice [1/2] (1): 1

...

✓ Prioritization complete!

Suggested next steps:
  1. Run with --output results.txt to save the prioritized list
  2. Re-run prioritization with different issues to refine rankings
```

## Input Format

The CSV file should contain one issue per row. The first column will be used as the issue description:

```csv
Fix authentication bug #123
Update API documentation #456
Improve performance of search #789
Add dark mode support #321
```

## Development

### Available Just Commands

```bash
just install          # Install dependencies
just install-dev      # Install with dev dependencies
just run INPUT        # Run the CLI
just format           # Format code with black
just lint             # Lint with ruff
just lint-fix         # Lint and auto-fix
just typecheck        # Type check with mypy
just check            # Run all quality checks
just test             # Run tests
just test-cov         # Run tests with coverage
just clean            # Clean build artifacts
just build            # Build package
```

### Code Quality

This project follows Python best practices:

- **Black** for code formatting (100 char line length)
- **Ruff** for fast linting
- **MyPy** for type checking
- **Pytest** for testing

Run all checks:
```bash
just check
```

## CLI Best Practices Implemented

✅ Clear, hierarchical help text with examples
✅ Consistent argument and option naming
✅ Sensible defaults and optional flags
✅ Rich error messages with context
✅ Colored output for better UX
✅ Progress indication during operations
✅ Exit codes for success/failure
✅ Verbose mode for debugging
✅ Version flag
✅ Input validation with helpful errors
✅ Suggestions for next steps after completion

## Architecture

Nightingale uses the **Command Pattern** for clean separation of concerns:

- `AcceptIssuesCommand` - Parses input from CSV or URL
- `PrioritizeIssuesCommand` - Binary insertion sort algorithm
- `CompareIssuesCommand` - Interactive user comparison
- `DisplayPrioritizedIssuesCommand` - Output formatting and display

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run quality checks (`just check`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Click](https://click.palletsprojects.com/) for CLI framework
- Styled with [Rich](https://rich.readthedocs.io/) for beautiful terminal output
- Managed with [UV](https://github.com/astral-sh/uv) for fast dependency management
- Task automation with [Just](https://github.com/casey/just)