class Node:
    """Node object"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked list object"""
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        """Adding new data to list"""

        # Creata a new Node
        new_node = Node(new_data)

        # Move the list head to the next position
        new_node.next = self.head

        # Add a new node to the list
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        """Adding new node after any nodes"""
        if prev_node is None:
            print("There is not node")
            return

        # Add new node
        new_node = Node(new_data)

        # Connection prev and next nodes
        prev_node.next = new_node

    def append(self, new_data):
        """Adding new node in the end of list"""

        # Create new node
        new_node = Node(new_data)

        # Checking list
        if self.head is None:
            # If not exist create a new
            self.head = new_node
            return

        # If check end of the list
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        """Delete value from list"""

        # Find head of list
        temp = self.head

        # Check if the first node has the key to be deleted
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Traverse the list to find the node with the key
        prev = None
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # If the value does not exist in the list
        if temp is None:
            return

        # Delete node from the list
        prev.next = temp.next
        temp = None
