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
        return '->'.join(nodes)

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        """ Returns the size of the list
        Time Complexity: O(n)
        """
        current = self.head
        count = 0

        while current:
            count = count + 1
            current = current.next_node

        return count

    def add(self, data) -> None:
        """Adds a Node containing data to the head of the LinkedList
        :param data: the data the Node that will be added contains.
        Time Complexity: O(1)
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key) -> Node:
        """ Searches the LinkedList for the first node that matches the key.
        :param key: search key for the data the Node is containing
        Returns the node or None if not found.
        :return the Node if found, else returns None
        Time Complexity O(n)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

        return None

    def insert(self, data, index) -> None:
        """ Inserts a new node containing data at position index.
        :param data: Data of the Node to be inserted
        :param index: Index at which the Node should be inserted
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

    def remove(self, key) -> Node:
        """Removes the first Node containing the data that matches the key
        :param key: Data of the Node to be deleted
        :return Node or None in case key is not found
        Time Complexity: O(n)
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node

            elif current.data == key:
                found = True
                previous.next_node = current.next_node

            else:
                previous = current
                current = current.next_node

        return current

    def remove_at_index(self, index: int) -> None:
        """ Removes the Node at the position with the index
        Index is 0-based
        :param index is the position at which the node should be deleted [0-Based]
        """
        ind = index
        current = self.head
        prev = None

        if index == 0:
            self.head = current.next_node

        while ind >= 0:
            if ind == 0:
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node

            ind -= 1

    def node_at_index(self, index: int) -> Node:
        """ Returns the Node at the position with the index
        Index is 0-based
        :param index is the position at which the node should be deleted [0-Based]
        :return Node
        """
        ind = 0
        current = self.head

        if index == 0:
            return self.head
        elif index > self.size():
            return None

        while ind < index:
            current = current.next_node
            ind += 1

        return current


l = LinkedList()
l.add(0)
l.add(1)
l.add(2)
l.add(3)
print(l.node_at_index(0))
print(l.node_at_index(2))
print(l.node_at_index(3))
print(l.node_at_index(12))
