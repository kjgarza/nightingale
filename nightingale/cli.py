"""
Nightingale CLI - GitHub Issue Prioritizer

A command-line tool for prioritizing GitHub issues using binary search comparison.
"""

import logging
import sys
from pathlib import Path

import click
from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel

from nightingale import nightingale

# Console for rich output
console = Console()

# Configure logging
def setup_logging(verbose: bool) -> None:
    """Configure logging with optional verbose output."""
    level = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(console=console, rich_tracebacks=True)]
    )


@click.command()
@click.argument(
    'input_source',
    type=str,
    metavar='INPUT'
)
@click.option(
    '-o', '--output',
    type=click.Path(path_type=Path),
    help='Output file path for prioritized issues. If not specified, results are printed to console.'
)
@click.option(
    '-v', '--verbose',
    is_flag=True,
    help='Enable verbose output for debugging.'
)
@click.option(
    '--version',
    is_flag=True,
    help='Show version and exit.'
)
@click.help_option('-h', '--help')
def main(input_source: str, output: Path | None, verbose: bool, version: bool) -> None:
    """
    Nightingale - Prioritize GitHub issues using interactive binary comparison.

    INPUT can be either:

    \b
    - Path to a CSV file containing GitHub issues
    - URL to a GitHub repository issue list

    The tool will interactively ask you to compare issues to determine priority.
    Results are displayed in order of importance (highest first).

    Examples:

    \b
        nightingale issues.csv
        nightingale https://github.com/user/repo/issues --output prioritized.txt
        nightingale issues.csv -v --output results.txt
    """

    if version:
        click.echo("Nightingale v0.2.0")
        return

    # Setup logging based on verbose flag
    setup_logging(verbose)
    logger = logging.getLogger(__name__)

    try:
        # Welcome message
        if not verbose:
            console.print(Panel.fit(
                "[bold blue]Nightingale[/bold blue] - GitHub Issue Prioritizer\n"
                "Interactive binary comparison for issue prioritization",
                border_style="blue"
            ))

        logger.debug(f"Input source: {input_source}")
        logger.debug(f"Output file: {output if output else 'console'}")
        logger.debug(f"Verbose mode: {verbose}")

        # Run the prioritization
        logger.info("Starting issue prioritization...")
        issues = nightingale.nightingale(input_source, output=output, verbose=verbose)

        # Success message with suggestions
        if issues:
            console.print("\n[bold green]✓[/bold green] Prioritization complete!", style="green")

            # Show next step suggestions
            console.print("\n[bold cyan]Suggested next steps:[/bold cyan]")
            if output:
                console.print(f"  1. Review prioritized issues in: [cyan]{output}[/cyan]")
                console.print(f"  2. Share results with your team or create a tracking board")
            else:
                console.print("  1. Run with [cyan]--output results.txt[/cyan] to save the prioritized list")
                console.print("  2. Re-run prioritization with different issues to refine rankings")

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        console.print(f"[bold red]Error:[/bold red] Input file not found: {input_source}", style="red")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error occurred: {e}", exc_info=verbose)
        console.print(f"[bold red]Error:[/bold red] {e}", style="red")
        if verbose:
            console.print_exception()
        sys.exit(1)


if __name__ == "__main__":
    main()