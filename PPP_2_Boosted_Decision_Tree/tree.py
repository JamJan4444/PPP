class Tree(object):
    def __init__(self):
        self.yes = None
        self.no = None
        self.data = None

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)