import pytest
from logic import generate_issues
from data import Issue

def test_generate_issues():
    issues = generate_issues()
    
    # There should be 5 issues
    assert len(issues) == 5

    # Each issue should have 'id', 'title' and 'description'
    # 'parent_id' should be None or an id of an existing issue
    for issue in issues:
        assert isinstance(issue, Issue)
        assert isinstance(issue.id, int)
        assert isinstance(issue.title, str)
        assert isinstance(issue.description, str)
        assert issue.parent_id == None or issues[issue.parent_id] is not None
