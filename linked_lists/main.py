from linked_list_func import Node
from linked_list_func import LinkedList


# Create a linked list
linked_list = LinkedList()

# Creata a 3 nodes
linked_list.head = Node("Monday")
seshanba = Node("Thuesday")
chorshanba = Node("Wednesday")

# Connecting nodes
linked_list.head.next = seshanba
seshanba.next = chorshanba

linked_list.push("Sunday")
linked_list.printList()
