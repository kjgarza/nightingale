# from nightingale.command import CompareIssuesCommand, PrioritizeIssuesCommand


# def test_compare_issues_command():
#     """
#     Test the CompareIssuesCommand class.
#     """

#     command = CompareIssuesCommand("Fix bug in login page", "Add new feature to dashboard")
#     assert command.execute() == "Add new feature to dashboard"

# def test_prioritize_issues_command():
#     """
#     Test the PrioritizeIssuesCommand class.
#     """

#     command = PrioritizeIssuesCommand(["Fix bug in login page", "Add new feature to dashboard", "Improve performance of search feature"])
#     assert command.execute() == ["Add new feature to dashboard", "Fix bug in login page", "Improve performance of search feature"]