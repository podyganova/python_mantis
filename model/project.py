from sys import maxsize


class Project:

    def __init__(self, name=None, status=None, enabled=None, view_status=None, description=None, id=None):
        self.name = name
        self.status = status
        self.enabled = enabled
        self.view_status = view_status
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s%s" % (self.id, self.name, self.description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               or self.name == other.name or self.description == other.description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
