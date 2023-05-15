from abc import ABC, abstractmethod

class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self):
        pass

class CompareIssuesCommand(Command):
    """
    The CompareIssuesCommand class implements the Command interface and
    compares two issues from the lists by asking which is more important.
    """

    def __init__(self, issue1, issue2):
        self.issue1 = issue1
        self.issue2 = issue2

    def execute(self):
        print(f"Which issue is more important?\n1. {self.issue1}\n2. {self.issue2}")
        response = input("Enter 1 or 2: ")
        if response == "1":
            return self.issue1
        elif response == "2":
            return self.issue2
        else:
            print("Invalid response. Please enter 1 or 2.")
            return None

class PrioritizeIssuesCommand(Command):
    """
    The PrioritizeIssuesCommand class implements the Command interface and
    uses a binary insert sort algorithm to prioritize the issues. uses  CompareIssuesCommand
    """

    def __init__(self, issues):
        self.issues = issues

    def execute(self):
        for i in range(1, len(self.issues)):
            j = i-1
            key = self.issues[i]
            while (j >= 0) and (CompareIssuesCommand(self.issues[j], key).execute() == key):
                self.issues[j+1] = self.issues[j]
                j -= 1
            self.issues[j+1] = key
        return self.issues
    
