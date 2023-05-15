class DisplayPrioritizedIssuesCommand:
    """
    The DisplayPrioritizedIssuesCommand class implements a command to display
    the prioritized list of issues.
    """

    def __init__(self, issues):
        self.issues = issues

    def execute(self):
        for i, issue in enumerate(self.issues):
            print(f"{i+1}. {issue}")