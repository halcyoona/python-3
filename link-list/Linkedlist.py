class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    
class Linklist:
    def __init__(self):
        self._start = None
        
    def insert(self, data):
        next_node = ListNode(data)
        
        if self._start is None:
            self._current = next_node
            self._start = next_node
        else:
            self._current.next = next_node
            self._current = next_node
