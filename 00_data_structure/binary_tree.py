class BinaryTree:
    def __init__(self, content, left=None, right=None):
        self.content = content
        self.left = left
        self.right = right
        
        self.depth = -1
        
    def __str__(self):
        return "(" + str(self.content) + " ( " + str(self.left) + " | "  \
    + str(self.right) + "))"