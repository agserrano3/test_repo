class Issue:
    def __init__(self, id, title, parent_id=None):
        self.id = id
        self.title = title
        self.parent_id = parent_id
