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

    def __repr__(self):
        """ Returns a string representation of the list
        Time Complexity: O(n)"""

        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return  '->'.join(nodes)

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
        """Adds a Node containing data to the head of the LinkedList
        Time Complexity: O(1)
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """ Searches the LinkedList for the first node that matches the key
        Returns the node or None if not found.
        Time Complexity O(n)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

        return None

    def insert(self, data, index):
        """ Inserts a new node containing data at position index.
        Insertion Time Complexity O(1)
        Getting to the Node Time Complexity O(1)
        Total Time Complexity O(n)
        """

        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev = current
            next_node = current.next_node

            prev.next = new
            new.next_node = next_node

    def remove(self, key):
        pass