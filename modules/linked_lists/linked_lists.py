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
        


# Challenge 8: Remove Duplicates
# Time: O(n) as we iterate through all nodes and do an O(1) lookup in a hashmap at each node
def remove_duplicates(lst):
    if lst.is_empty():
        return False
    
    dup_dict = {}
    prev_node = lst.get_head()
    dup_dict[str(prev_node.data)] = True
    cur_node = prev_node.next_element
    while cur_node:
        if not dup_dict.get(str(cur_node.data)):
            dup_dict[str(cur_node.data)] = True
            prev_node.next_element = cur_node
            prev_node = cur_node
            print(str(cur_node.data) + " doesn't exist, incrementing previous node")
        else: 
            print(str(cur_node.data) + " exists, skipping")
            prev_node.next_element = cur_node.next_element

        cur_node = cur_node.next_element

    return lst

# Time: O(n)
def get_tail_node(lst):
    cur_node = lst.get_head()
    while cur_node.next_element:
        cur_node = cur_node.next_element
    return cur_node

# Challenge 9(a): Union of Linked Lists
# Time: O(2(n+m)) as we are first iterating the first list to find the tail, and then iterating the second list to add its nodes to the tail, and then removing duplicates from the combined lists
def union(list1, list2):
    # Link both lists
    get_tail_node(list1).next_element = list2.get_head()
    # Remove duplicates and return
    return remove_duplicates(list1)

# Challenge 9(b): Intersection of Linked Lists
# Time: O(n + m) for removing duplicates, O(n*m) for finding intersections
def intersection(list1, list2):
    # remove duplicates from both lists
    list1 = remove_duplicates(list1)
    list2 = remove_duplicates(list2)
    if not list1 or not list2:
        return None
    # Iterate through list1 and compare each node with all nodes in list 2
    # if the node doesn't exist in list2 aswell, delete it from the list
    prev_node = list1.get_head()
    cur_node = prev_node.next_element
    while cur_node:
        if not list2.search(cur_node.data):
            prev_node.next_element = cur_node.next_element
        prev_node = cur_node
        cur_node = cur_node.next_element

    return list1


# Challenge 10: Return Nth node from End
# Time: O(n) to reverse the list, O(n) to iterate n nodes from the end (now start)
### SHOULD HAVE USED LENGTH AND SUBTRACTED N RATHER THAN REVERSE!
def find_nth(lst, n):
    # reverse lst
    lst = reverse(lst)
    lst.print_list()
    print(n)
    count = 1
    cur_node = lst.get_head()
    # while count < n iterate through nodes, if count > n, return -1
    while count < n:
        if cur_node.next_element:
            cur_node = cur_node.next_element
        else:
            return -1
        count += 1
    return cur_node.data
