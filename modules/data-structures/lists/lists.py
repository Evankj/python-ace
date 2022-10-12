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
    for i in range(len(lst)):
        if i+k < len(lst):
            new_lst[i+k] = lst[i]
        else:
            new_lst[int((i+k)%len(lst))] = lst[i]
    return new_lst
        
# Challenge 9: Rearrange Positive and Negative Values
# Approach: Two pointers? One going from front of list stopping on positives and a second going from back stopping on negatives
# When both pointers are stopped, swap their values and proceed
# Time: O(n) as we iterate through the whole list from both ends (but stop when pointers meet)
def rearrange(lst):
    neg_index = 0
    pos_index = len(lst)-1


    while neg_index < pos_index:
        front_val = lst[neg_index]
        rear_val = lst[pos_index]
        if front_val < 0:
            # didn't find a pos, increment pointer
            neg_index += 1
        if rear_val >= 0:
            # didn't find a neg, decrement pointer
            pos_index -= 1

        if front_val >= 0 and rear_val < 0:
            # we need to swap these values and inc/dec both pointers
            lst[neg_index] = rear_val
            lst[pos_index] = front_val
            neg_index += 1
            pos_index -= 1

    return lst

# Challenge 10: Rearrange Sorted List in Max/Min Form
# Approach: even indices will be descending, odd incices will be ascending.
# odd = 0 = len - 1, 2 = len - 3, len - 5 
# even = 1, 3, 5
def max_min(lst):
    if len(lst) <= 0:
        return lst

    start_index = 0
    end_index = len(lst)-1
    max_val = lst[end_index]
    min_val = lst[start_index]
    for i in range(len(lst)):
        # Even = Descending
        if i % 2 == 0:
            lst[i] = max_val
            end_index -= 2
            max_val = lst[end_index]
        else:
            lst[i] = min_val
            start_index += 2
            min_val = lst[start_index]
        return lst   

# Challenge 11: Maximum Sum Sublist
# Approach: Sliding window -> check 1st elem, store as max sum, check 1st + 2nd, if greater, store as max sum, else drop first elem, check just 2nd elem, if greater store as sum, else check 2nd + 3rd and continue 
def find_max_sum_sublist(lst):
    print(lst)
    if len(lst) <= 0:
        return lst

    window_start_index = 0
    window_end_index = 0
    max_sum = lst[0]
    cur_sum = max_sum

    for i in range(len(lst)):
        print('''

            Sum: {0}
            Start Index: {1}
            End Index: {2}
            Contains: {3}


        '''.format(cur_sum, window_start_index, window_end_index, lst[window_start_index:window_end_index+1]))
        if cur_sum <= max_sum:
            window_end_index += 1
            cur_sum+=lst[window_end_index]
            print("Added " + str(lst[window_end_index]))
        else:
            cur_sum-=lst[window_start_index]
            print("Subtracted " + str(lst[window_start_index]))
            window_start_index += 1
            max_sum = cur_sum
    return max_sum



if __name__ == "__main__":
   print(right_rotate([10,20,30,40,50], 3))
