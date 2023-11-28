import os
from .accept_issues_command import AcceptIssuesCommand
from .command import PrioritizeIssuesCommand
from .display_prioritized_issues_command import DisplayPrioritizedIssuesCommand

def nightingale(input):
   issues = AcceptIssuesCommand(input).execute()
   issues = PrioritizeIssuesCommand(issues).execute()
   DisplayPrioritizedIssuesCommand(issues).execute()
   return issues

