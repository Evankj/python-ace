from LinkedList import LinkedList
from Node import Node

# Challenge 1: Insertion at Tail
# Time: O(n) as we iterate through all nodes to get to final node (singly linked list)
def insert_at_tail(lst, value):
    tail_node = Node(value)
    if lst.is_empty():
        lst.head_node = tail_node
        return

    cur_node = lst.get_head()
    while cur_node.next_element:
        cur_node = cur_node.next_element

    cur_node.next_element = tail_node
    return


# Challenge 2: Search in a Singly Linked List
# Time: O(n) as we search iteratively from head to tail to find node with data == value
def search(lst, value):
    if lst.is_empty():
        return False

    cur_node = lst.get_head()
    while cur_node:
        if cur_node.data == value:
            return True
        cur_node = cur_node.next_element

    return False

# Challenge 3: Deletion by Value
# Time: O(n) as we search iteratively from head to tail to find node with data == value and delete it
def delete(lst, value):
    if lst.is_empty():
        return False

    cur_node = lst.get_head()
    # Check if head node is deletion node
    if cur_node.data == value:
        # Will be None if next element doesn't exists
        lst.head_node = cur_node.next_element
        return True

    while cur_node:
        next_node = cur_node.next_element
        if next_node:
            if next_node.data == value:
                cur_node.next_element = next_node.next_element
                return True
        cur_node = cur_node.next_element

    return False

# Challenge 4: Find the Length of a Linked List
# Time: O(n) as we iterate through all nodes to increment count
def length(lst):
    length = 0
    cur_node = lst.get_head()
    while cur_node:
        length += 1
        cur_node = cur_node.next_element

    return length

# Challenge 5: Reverse a Linked List
# Time: O(n) as we traverse the whole linked list
def reverse(lst):
    cur_node = lst.get_head()
    prev_node = None
    next_node = None
    while cur_node:
        next_node = cur_node.next_element
        cur_node.next_element = prev_node
        prev_node = cur_node
        cur_node = next_node
        lst.head_node = prev_node

    return lst

# Challenge 6: Detect Loop in a Linked List --- NOT WORKING, INCORRECT IMPLEMENTATION
# Time: O(n) as we traverse the loop once over 
def detect_loop(lst):
    # Initialise both pointers at head
    cur_node_single = lst.get_head()
    cur_node_double = cur_node_single
    while cur_node_single:
        next_node = cur_node_single.next_element
        if next_node:
            next_double = next_node.next_element
            if next_node == next_double:
                return True
            cur_node_double = next_double
        cur_node_single = next_node
    
    return False

# Challenge 7: Find Middle Node of Linked List
# Time: O(1.5n) as we iterate once over to find length, and then again over half the list to get the middle node, surely there's a better way to do this?
def find_mid(lst):
    length = lst.length() - 1
    if length <= 0:
        return False
    mid_count = (length/2 + 1, length/2)[length % 2 == 0]
    count = 0
    mid_node = lst.get_head()
    while count < mid_count:
        mid_node = mid_node.next_element
        count += 1
    return mid_node.data
        


    

