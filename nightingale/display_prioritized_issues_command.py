"""Command for displaying prioritized issues."""

import logging
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()
logger = logging.getLogger(__name__)


class DisplayPrioritizedIssuesCommand:
    """
    The DisplayPrioritizedIssuesCommand class implements a command to display
    the prioritized list of issues.
    """

    def __init__(self, issues: list, output: Path | None = None, verbose: bool = False):
        """
        Initialize the display command.

        Args:
            issues: List of prioritized issues
            output: Optional file path to write results
            verbose: Enable verbose logging
        """
        self.issues = issues
        self.output = output
        self.verbose = verbose

    def execute(self) -> None:
        """
        Execute the display command.

        Displays issues to console or writes to file based on configuration.
        """
        if not self.issues:
            logger.warning("No issues to display")
            console.print("[yellow]No issues to display[/yellow]")
            return

        logger.debug(f"Displaying {len(self.issues)} prioritized issues")

        if self.output:
            # Write to file
            self._write_to_file()
        else:
            # Display to console
            self._display_to_console()

    def _write_to_file(self) -> None:
        """Write prioritized issues to output file."""
        try:
            output_path = Path(self.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write("Prioritized GitHub Issues\n")
                f.write("=" * 80 + "\n\n")

                for i, issue in enumerate(self.issues, 1):
                    f.write(f"{i}. {issue}\n")

            logger.info(f"Results written to {output_path}")
            console.print(f"\n[green]✓[/green] Results saved to: [cyan]{output_path}[/cyan]")

        except IOError as e:
            logger.error(f"Failed to write to output file: {e}")
            console.print(f"[red]Error writing to file: {e}[/red]")

    def _display_to_console(self) -> None:
        """Display prioritized issues in console with rich formatting."""
        table = Table(title="\nPrioritized Issues (Highest Priority First)", show_header=True)
        table.add_column("Priority", style="cyan", justify="right", width=8)
        table.add_column("Issue", style="white")

        for i, issue in enumerate(self.issues, 1):
            # Color code by priority
            if i == 1:
                priority_style = "bold red"
            elif i <= 3:
                priority_style = "bold yellow"
            else:
                priority_style = "green"

            table.add_row(
                f"[{priority_style}]#{i}[/{priority_style}]",
                issue
            )

        console.print(table)