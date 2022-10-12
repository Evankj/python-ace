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

# Challenge 4: In-order Successor of Binary Search Tree
def find_inorder_successor(root, node_value):

    return None

# Challenge 6: Level Order Traversal of Binary Tree (BFS)
def level_order_traversal(root):
    result = ""
    
    if not root or (not root.left and not root.right):
        # result = str(root.data)
        print(result, end="")
        return

    queue = [root]

    while len(queue) > 0:
        # Items in the queue are a "level"
        next_queue = []
        for node in queue:
            result += str(node.data) + ', '
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue

    print(result, end="")
