import math
from timeit import default_timer as timer


# Challenge 1: Remove Even Integers from a List
# My approach: Use list comprehension to iterate through list contents and return a new list consisting only of elements that are not even (divisible by 2)
# Time: O(n), every element is iterated over once
def remove_even(lst):
    return [x for x in lst if x % 2 != 0]


# Challenge 2: Remove Even Integers from a List
# My approach: Compare first index of both lists and add the lowest, then remove it from whichever list it was taken from
# Time: O(n+m) MAX as each index of both lists is only compared once, and if one list is emptied, the other is simply appended to the returned list so may be lower than O(n+m) dependent on inputs
def merge_lists(lst1, lst2):
    merged_lst = []
    while (len(lst1) + len(lst2)) > 0:
        if 0 in [len(lst1), len(lst2)]:
            merged_lst += (lst1 + lst2)
            lst1, lst2 = [], []
        else:
            lst1_val = lst1[0]
            lst2_val = lst2[0]
            if lst1_val < lst2_val:
                merged_lst += [lst1_val]
                lst1 = lst1[1:]
            else:
                merged_lst += [lst2_val]
                lst2 = lst2[1:]

    return merged_lst


# Challenge 3: Find Two Numbers that Add up to "k"
# My approach: Increment index and compare with all remaining elements
# Time: O(n!) MAX as each element is compared with all elements with a higher index then itself???
def find_sum(lst, k):
    start_index = 0
    compare_index = 1
    
    pair = [lst[start_index], lst[compare_index]]
    count = 0

    while sum(pair) != k and start_index < (len(lst)-1):
        if (compare_index < len(lst)-1):
            compare_index += 1
        else:
            start_index += 1
            if (start_index > len(lst)-2):
                return False
            compare_index = start_index + 1
        pair = [lst[start_index], lst[compare_index]]
        count += 1
    return pair, count


# Challenge 4: List of Products of all Elements
# My approach: Nested for loops, skipping the top loop's index and finding the product of the other elements
# Time: O((n)*(n-1/2)) == O(n^2)
def find_product(lst):
    prod_lst = []
    for idx, i in enumerate(lst):
        product = 1
        for idx, j in enumerate(lst):
            if (i != j):
                product *= j
        prod_lst += [product]
    return prod_lst

# Challenge 5: Find Minimum Value in List
# My approach: Iterate over each element and compare to current smallest value
# Time: O(n) as each element is iterated over once
def find_minimum(lst):
    lst_len = len(lst)
    if lst_len <= 0:
        return False
    if lst_len == 1:
        return lst[0]
    cur_min = lst[0]
    for num in lst[1:]:
        if num < cur_min:
            cur_min = num
    return cur_min


# Challenge 6: First Non-Repeating Integer in a list
# My approach: Compare each element with next element, if element on left is same, mark as repeating, if element on left is dif and element on right is dif, return middle element
# Time: O(n) as each element is iterated over once
def find_first_unique(lst):
    lst_len = len(lst)
    if lst_len <= 0:
        return False
    if lst_len == 1:
        return lst[0]
    if lst_len == 2:
        return (False, lst[0])[lst[0] != lst[1]]
    for i in range(1,lst_len):
        left = i-1
        right = (False, i+1)[i+1 <= lst_len]
        if (right):
            if left != lst[i] and right != lst[i]:
                return lst[i]
        else:
            if left != lst[i]:
                return lst[i]
    return False       

# Challenge 8: Right Rotate List
# Time: O(n) as we iterate the whole list
def right_rotate(lst, k):
    # initialise a new list with dummy values
    new_lst = [None] * len(lst)

    new_lst = [None] * len(lst)
    for i in range(len(lst)):
        if i+k < len(lst):
            new_lst[i+k] = lst[i]
        else:
            new_lst[int((i+k)%len(lst))] = lst[i]
    return new_lst
        
# Challenge 9: Rearrange Positive and Negative Values
# Approach: Two pointers? One going from front of list stopping on positives and a second going from back stopping on negatives
# When both pointers are stopped, swap their values and proceed
def rearrange(lst):
    neg_index = 0
    pos_index = len(lst)-1

    for i in range(len(lst)):
        front_val = lst[neg_index]
        rear_val = lst[pos_index]

        if front_val >= 0:
            # found a pos, leave pointer here
            pass
        if rear_val < 0:
            # found a neg, leave pointer here
            pass

if __name__ == "__main__":
   print(right_rotate([10,20,30,40,50], 3))
