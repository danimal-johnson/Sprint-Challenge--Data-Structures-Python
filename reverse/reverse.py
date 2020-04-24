class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        if self.head == None:
            # Empty list
            return
        if self.head.get_next() == None:
            # List length of 1 is already sorted
            return

        if node.get_next() == None:
            # Boundary condition: end of list
            # Point the head to here and return
            self.head = node
            return

        # Recursive call to sort list from next node
        self.reverse_list(node.get_next(), None)

        # On the way back out of the recursion.
        # (Reverse the pointers.)
        # Set the next node's next_node to this node
        node.next_node.set_next(node)
        # Now set this node's pointer to null
        node.set_next(None)

# For testing:
# back = LinkedList()
# back.add_to_head(1)
# back.add_to_head(2)
# back.add_to_head(3)
# back.add_to_head(4)
# back.add_to_head(5)
