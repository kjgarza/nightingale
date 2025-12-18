import argparse
import sys
from nightingale import nightingale


def print_help():
    """Display comprehensive help information for the nightingale CLI."""
    help_text = """
Nightingale - GitHub Issues Prioritizer
========================================

A tool to prioritize GitHub issues using binary insert sort algorithm.

USAGE:
    nightingale <input> [OPTIONS]
    nightingale help

COMMANDS:
    help                    Display this help information

ARGUMENTS:
    <input>                 CSV file with GitHub issues names and links 
                           or URL to GitHub repo issue list

OPTIONS:
    -o, --output <file>    Output file for prioritized issues
    -v, --verbose          Print verbose output
    -h, --help             Show help message and exit

EXAMPLES:
    # Prioritize issues from a local CSV file
    nightingale issues.csv

    # Prioritize issues from a URL
    nightingale https://example.com/issues.csv

    # Save prioritized issues to a file
    nightingale issues.csv -o prioritized.csv

    # Run with verbose output
    nightingale issues.csv -v

HOW IT WORKS:
    The tool will present you with pairs of issues and ask you to choose
    which one is more important. Based on your choices, it will build a
    prioritized list using a binary insert sort algorithm.

    For each comparison, enter:
    - '1' to select the first issue as more important
    - '2' to select the second issue as more important

For more information, visit: https://github.com/kjgarza/nightingale
"""
    print(help_text)


def main():
    # Check if 'help' command is provided
    if len(sys.argv) > 1 and sys.argv[1] == 'help':
        print_help()
        sys.exit(0)

    parser = argparse.ArgumentParser(
        description="Prioritize GitHub issues using interactive comparisons",
        epilog="Use 'nightingale help' for more detailed information"
    )

    parser.add_argument("input", help="CSV file with GitHub issues names and links or URL to GitHub repo issue list")
    parser.add_argument("-o", "--output", help="Output file for prioritized issues")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print verbose output")

    args = parser.parse_args()
    nightingale.nightingale(args.input)

    print(args)

if __name__ == "__main__":
    main()