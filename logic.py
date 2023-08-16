import random
from data import Issue

def generate_issues():
    # Create five unique issues
    issues = [Issue(i, f"Issue #{i}") for i in range(5)]

    # Randomly assign parent_ids
    for issue in issues:
        parent = random.choice([None] + issues)
        if parent is not None:
            issue.parent_id = parent.id

    # Print the tree structure of issues
    for issue in issues:
        parent_issue = next((x for x in issues if x.id == issue.parent_id), None)
        if issue.parent_id is None:
            print(f"Issue id={issue.id}, title='{issue.title}', has no parent issue")
        else:
            print(f"Issue id={issue.id}, title='{issue.title}', parent issue id={parent_issue.id}, parent issue title='{parent_issue.title}'")

# Call the function to generate and print issues
generate_issues()
