"""Command for accepting and parsing GitHub issues from various sources."""

import csv
import logging
from pathlib import Path

import requests

logger = logging.getLogger(__name__)


class AcceptIssuesCommand:
    """
    The AcceptIssuesCommand class implements a command to accept a CSV with
    GitHub issues names and links or a URL to GitHub repo issue list as an
    initial step.
    """

    def __init__(self, input_file: str, verbose: bool = False):
        """
        Initialize the command.

        Args:
            input_file: Path to CSV file or URL to GitHub issues
            verbose: Enable verbose logging
        """
        self.input_file = input_file
        self.verbose = verbose

    def execute(self) -> list:
        """
        Execute the command to load issues.

        Returns:
            List of issues loaded from the input source

        Raises:
            FileNotFoundError: If the input file doesn't exist
            requests.HTTPError: If URL download fails
        """
        issues = []

        if self.input_file.startswith("http"):
            logger.debug(f"Downloading issues from URL: {self.input_file}")
            # Download the CSV file from the URL
            try:
                response = requests.get(self.input_file, timeout=30)
                response.raise_for_status()
                csv_data = response.text
                logger.debug(f"Downloaded {len(csv_data)} bytes")
            except requests.RequestException as e:
                logger.error(f"Failed to download from URL: {e}")
                raise
        else:
            logger.debug(f"Reading issues from file: {self.input_file}")
            # Read the CSV file from disk
            file_path = Path(self.input_file)
            if not file_path.exists():
                raise FileNotFoundError(f"File not found: {self.input_file}")

            with open(file_path, "r", encoding="utf-8") as f:
                csv_data = f.read()
                logger.debug(f"Read {len(csv_data)} bytes from file")

        # Parse the CSV data
        reader = csv.reader(csv_data.splitlines())
        for i, row in enumerate(reader):
            if row:  # Skip empty rows
                issues.append(row[0])
                if self.verbose:
                    logger.debug(f"Loaded issue {i+1}: {row[0][:50]}...")

        logger.info(f"Successfully loaded {len(issues)} issues")
        return issues