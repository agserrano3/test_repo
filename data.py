class Issue:
    def __init__(self, id, title, description='', parent_id=None):
        self.id = id
        self.title = title
        self.description = description
        self.parent_id = parent_id

