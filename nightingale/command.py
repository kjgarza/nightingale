"""Command classes for issue prioritization."""

import logging
from abc import ABC, abstractmethod

from rich.console import Console
from rich.prompt import Prompt

console = Console()
logger = logging.getLogger(__name__)


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass


class CompareIssuesCommand(Command):
    """
    The CompareIssuesCommand class implements the Command interface and
    compares two issues from the lists by asking which is more important.
    """

    def __init__(self, issue1: str, issue2: str, verbose: bool = False):
        """
        Initialize the comparison command.

        Args:
            issue1: First issue to compare
            issue2: Second issue to compare
            verbose: Enable verbose logging
        """
        self.issue1 = issue1
        self.issue2 = issue2
        self.verbose = verbose

    def execute(self) -> str | None:
        """
        Execute the comparison by prompting the user.

        Returns:
            The selected issue (issue1 or issue2), or None if invalid input
        """
        console.print("\n[bold yellow]Which issue is more important?[/bold yellow]")
        console.print(f"[cyan]1.[/cyan] {self.issue1}")
        console.print(f"[cyan]2.[/cyan] {self.issue2}")

        while True:
            response = Prompt.ask(
                "Enter your choice",
                choices=["1", "2"],
                default="1"
            )

            if response == "1":
                logger.debug(f"User selected issue 1: {self.issue1[:50]}...")
                return self.issue1
            elif response == "2":
                logger.debug(f"User selected issue 2: {self.issue2[:50]}...")
                return self.issue2
            else:
                console.print("[red]Invalid response. Please enter 1 or 2.[/red]")


class PrioritizeIssuesCommand(Command):
    """
    The PrioritizeIssuesCommand class implements the Command interface and
    uses a binary insert sort algorithm to prioritize the issues using CompareIssuesCommand.
    """

    def __init__(self, issues: list, verbose: bool = False):
        """
        Initialize the prioritization command.

        Args:
            issues: List of issues to prioritize
            verbose: Enable verbose logging
        """
        self.issues = issues
        self.verbose = verbose
        self.comparison_count = 0

    def binary_search(self, arr: list, key: str, start: int, end: int) -> int:
        """
        Perform binary search to find the correct position for key in sorted array.

        Args:
            arr: Sorted array to search in
            key: Item to find position for
            start: Start index
            end: End index

        Returns:
            Index where key should be inserted
        """
        if start == end:
            return start

        mid = (start + end) // 2
        self.comparison_count += 1

        if self.verbose:
            logger.debug(f"Binary search: comparing position {mid} (total comparisons: {self.comparison_count})")

        comparison = CompareIssuesCommand(arr[mid], key, verbose=self.verbose).execute()

        if comparison != key:
            # arr[mid] is more important, search right half
            return self.binary_search(arr, key, mid + 1, end)
        elif comparison == key:
            # key is more important, search left half
            return self.binary_search(arr, key, start, mid)
        else:
            return mid

    def execute(self) -> list:
        """
        Execute the prioritization using binary insertion sort.

        Returns:
            Sorted list of issues (highest priority first)
        """
        if len(self.issues) <= 1:
            logger.info("Only one or zero issues, no prioritization needed")
            return self.issues

        logger.info(f"Starting binary insertion sort for {len(self.issues)} issues")

        for i in range(1, len(self.issues)):
            key = self.issues[i]
            logger.debug(f"Processing issue {i+1}/{len(self.issues)}")

            # Find the correct position using binary search
            j = self.binary_search(self.issues, key, 0, i)

            # Remove the key from its current position
            self.issues = self.issues[:i] + self.issues[i+1:]
            # Insert the key at the correct position
            self.issues = self.issues[:j] + [key] + self.issues[j:]

        logger.info(f"Prioritization complete with {self.comparison_count} comparisons")
        return self.issues

