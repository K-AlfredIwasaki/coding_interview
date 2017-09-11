class LinkedList:
    def __init__(self,content):
        self.content = content
        self.next = None

    def __str__(self):
        return "( " + str(self.content) + str(self.next) + " )"