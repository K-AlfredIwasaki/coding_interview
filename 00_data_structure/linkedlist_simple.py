class LinkedList:
    def __init__(self,content):
        self.content = content
        self.next = None

    def __str__(self):

    	current = self
    	result = []
    	while current != None:
    		result.append(str(current.content))
    		current = current.next

    	return "=>".join(result)


