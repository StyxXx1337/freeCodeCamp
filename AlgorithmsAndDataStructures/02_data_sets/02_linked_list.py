class Node:
    """An object for storing a single node of a linked list.
    Has 2 attributes
    Data : (int)
    next_node : (Node)
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """Single Linked List
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """ Returns the size of the list
        Time Complexity: O(n)
        """
        current = self.head
        count = 0

        while current:
            count = count + 1
            current = current.next_node

        return count

    def add(self, data):
        """Adds a Node to the head of the LinkedList
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

