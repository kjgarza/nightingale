import csv
import requests

class AcceptIssuesCommand:
    """
    The AcceptIssuesCommand class implements a command to accept a CSV with
    GitHub issues names and links or a URL to GitHub repo issue list as an
    initial step.
    """

    def __init__(self, input_file):
        self.input_file = input_file

    def execute(self):
        issues = []
        if self.input_file.startswith("http"):
            # Download the CSV file from the URL
            response = requests.get(self.input_file)
            response.raise_for_status()
            csv_data = response.text
        else:
            # Read the CSV file from disk
            with open(self.input_file, "r") as f:
                csv_data = f.read()

        # Parse the CSV data
        reader = csv.reader(csv_data.splitlines())
        for row in reader:
            issues.append(row[0])

        return issues