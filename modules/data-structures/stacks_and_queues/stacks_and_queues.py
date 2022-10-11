from Queue import MyQueue
from Stack import MyStack

# Challenge 3: Reversing First K Elements of Queue
# Time: O(n) as we iterate through k entries to create the stack (though we do this twice, once in the creation and again in the queue rebuild :/ ), and then n-k entries to rebuild the queue
def reverseK(queue, k):
    # Create a stack
    # dequeue k elements, storing each in stack
    # queue all elements from stack back to queue
    # dequeue then immediately queue len(queue)-k elements from queue
    
    # handle edge cases
    if k > queue.size() or k < 0 or queue.is_empty():
        return None

    # Create a stack
    stack = MyStack()

    # dequeue k elements, storing each in stack
    for i in range(k):
        # Do as two separate steps as queue.dequeue() returns just the value, not the Node (see DoublyLinkedList.py)
        stack.push(queue.front())
        queue.dequeue()

    # queue all elements from stack back to queue
    while not stack.is_empty():
        # again, do as two separate steps as I'm not sure if builtin list pop() returns the popped list item
        queue.enqueue(stack.peek())
        stack.pop()

    # dequeue then immediately queue len(queue)-k elements from queue
    for i in range(queue.size()-k):
        # Again, two separate steps as I didn't test if dequeue() returns a Node
        queue.enqueue(queue.front())
        queue.dequeue()

    return queue



# Challenge 4: Implement Queue using Stacks
# I misunderstood and thought we were required to dequeue/enqueue from the bottom of the stack
class NewQueue:

    def __init__(self):
        self.main_stack = MyStack()

    # Inserts Element in the Queue
    # To enqueue, create a new stack and pop all elements from main stack and push them to new stack
    # next push value to main stack and then pop all elements from new stack and push them to main stack
    def enqueue(self, value):
        new_stack = MyStack()
        while not self.main_stack.is_empty():
            new_stack.push(self.main_stack.pop())

        while not new_stack.is_empty(): 
            self.main_stack.push(new_stack.pop())
        self.main_stack.push(value)


    # Removes Element From Queue
    # To dequeue, create a new stack and pop size-1 times from main_stack and push into new stack, then pop final element from main_stack but don't push it to the new_stack
    # next pop every element from new stack and push it back to main_stack (which should be empty)
    def dequeue(self):
        new_stack = MyStack()
        for i in range(self.main_stack.size()-1):
            new_stack.push(self.main_stack.pop())
        remove = self.main_stack.pop()
        while not new_stack.is_empty():
            self.main_stack.push(new_stack.pop())
        return remove


# Challenge 6: Evaluate Postfix Expression Using a Stack
# Construct a stack,
# foreach char in expression, if char is number, push into stack, if is expression, pop two elements from stack and run them through the expression
# Add the result to return value
def evaluate_post_fix(exp):
    value = 0
    stack = MyStack()
    for char in exp:
        if char.isnumeric():
            stack.push(int(char))
        else:
            if char != ' ':
                rhs = stack.pop()
                lhs = stack.pop()
                if lhs and rhs:
                    res = 0
                    if char == '+':
                        res += lhs + rhs
                    if char == '*':
                        res += lhs * rhs
                    if char == '-':
                        res += lhs - rhs
                    if char == '/':
                        res += lhs / rhs
                    stack.push(res)
                    value += res
    return value


# Challenge 7: Next Greater Element Using a Stack
# Naive approach: Iterate through list and compare with remaining elements in list, if higher, push to stack, else continue iterating. Push -1 to stack if no more elements in list to compare to
def next_greater_element(lst):
    stack = MyStack()
    ret_lst = []
    index = 1
    for element in lst:
        stack_size = stack.size()
        compare_index = index
        while compare_index < len(lst) and stack.size() == stack_size:
            if (element < lst[compare_index]):
                stack.push(lst[compare_index])
                ret_lst.append(lst[compare_index])
            compare_index += 1
        if compare_index == len(lst):
            stack.push(-1)
            ret_lst.append(-1)
        index += 1


    return ret_lst

# Challenge 8: Implement O(1) min() Function for Stack
# Approach: Use a stack to track min vals
class MinStack:
    # Constructor
    def __init__(self):
        # Write your code here
        self.stack = MyStack()
        self.min_stack = MyStack()

    def pop(self):
        if self.stack.peek() == self.min_stack.peek():
            self.min_stack.pop()
        self.stack.pop()

    # Pushes value into new stack
    def push(self, value):
        self.stack.push(value)
        if self.min_val:
            if self.min_val > value:
                self.prev_min_val = self.min_val
                self.min_val = value
        else:
            self.min_val = value

    # Returns minimum value from new stack in constant time
    def min(self):
        return self.min_val

    # Write any helper functions here


