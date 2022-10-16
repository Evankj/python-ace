from binary_tree import *
from binary_tree_node import *
    
# Challenge 1: Determine if two binary trees are identical
def are_identical(root1, root2):
    if not root1 and not root2:
        return True
    if (not root1 and root2) or (not root2 and root1):
        return False

    if(root1.data == root2.data):
        lefts_match = are_identical(root1.left, root2.left)
        rights_match = are_identical(root1.right, root2.right)
        return lefts_match and rights_match
    return False

# Challenge 2: Write an In-Order Iterator for a Binary Tree
# This solution doesn't correctly account for LHS nodes...
class InorderIterator:
    def __init__(self, root):
        self.stack = self.fill_stack(root)

    def fill_stack(self, root):
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        return stack
                
    def peek_stack(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def hasNext(self):
        return(self.peek_stack() != None)

    def getNext(self):
        if self.hasNext():
            next = self.stack.pop(len(self.stack)-1)

            if next.right:
                self.stack.append(next.right)
            return(next)
        return None

# Iterator helper function (Don't modify it)
# This function returns the in-order list of nodes using the hasNext() and
# getNext() methods
def inorder_using_iterator(root):
    iter = InorderIterator(root)
    result = ""
    while iter.hasNext():
        ptr = iter.getNext()
        if iter.hasNext():
            result += str(ptr.data) + ", "
        else:
            result += str(ptr.data)
    if result == "":
        result = "None"
    return result


# Challenge 3: Iterative In-Order Traversal of Binary Tree
# Approach: Similar to Challenge 2, fill stack with all left hand elements first, then iterate through the stack.
# if the node in the stack has a right element, add it to the stack
# TODO: Figure out why this and Challenge 2 solution doesn't like test case 1 125 val (not appending node.left I'm guessing?)
def inorder_iterative(root):
    if not root:
        print("None")
        return

    result = ""
    node = root
    stack = []
    # fill stack with left nodes
    while node:
        stack.append(node)
        node = node.left

    while len(stack) > 0:
        node = stack.pop(len(stack)-1)
        result += str(node.data) + ", "
        if node.right:
            stack.append(node.right)

    # HACK: Dirty hack to remove last comma
    if result.endswith(","):
        result = result[:len(result)-2]

    print(result, end="") 

def find_lowest(root):
    while root:
        root = root.left

 

def get_lowest_node(root):
    # if no root, return none
    if not root:
        return None

    node = root
    left = node.left
    right = node.right
    while left or right:
        # while node has children
        # if node has a left child, set node to left, if not, set node to right
        # if node has no children, exit loop and return node
        if left:
            node = left
        else:
            if right:
                node = right
        left = node.left
        right = node.right

    return node

# Challenge 4: In-order Successor of Binary Search Tree
# This is a BST not just a Binary Tree, therefore "the in-order successor of a node in a BST is the node with the smallest 
# key greater than the key of the current node. This is the same as the next node in an in-order traversal of the BST."
def find_inorder_successor(root, node_value):
    value = -1
    return None



# Challenge 5: In-order Successor Binary Search Tree With Parent Pointers
def find_inorder_successor(root, predecessor_data)
def get_lowest_left_val(root):
    while root:
        root = root.left
    return root



# Challenge 7: Reverse Level Order Traversal
# Apprach: Use a stack and dummy node
def traverse(root):
    if not root:
        return None

    result = []
    visited_stack = []
    queue = [root]
    while len(queue) > 0:
        node = queue.pop
        pass



    return result
