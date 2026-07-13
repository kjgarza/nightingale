"""Main nightingale orchestration module."""

import logging
from pathlib import Path

from .accept_issues_command import AcceptIssuesCommand
from .command import PrioritizeIssuesCommand
from .display_prioritized_issues_command import DisplayPrioritizedIssuesCommand

logger = logging.getLogger(__name__)


def nightingale(input_source: str, output: Path | None = None, verbose: bool = False) -> list:
    """
    Main orchestration function for issue prioritization.

    Args:
        input_source: CSV file path or URL to GitHub issues
        output: Optional output file path for results
        verbose: Enable verbose logging

    Returns:
        List of prioritized issues
    """
    logger.debug(f"Processing input: {input_source}")

    # Step 1: Accept and parse issues
    issues = AcceptIssuesCommand(input_source, verbose=verbose).execute()
    logger.info(f"Loaded {len(issues)} issues")

    # Step 2: Prioritize issues through binary comparison
    issues = PrioritizeIssuesCommand(issues, verbose=verbose).execute()
    logger.info("Issues prioritized successfully")

    # Step 3: Display or save prioritized issues
    DisplayPrioritizedIssuesCommand(issues, output=output, verbose=verbose).execute()

    return issues

