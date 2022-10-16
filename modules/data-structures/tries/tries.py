from Trie import Trie
from TrieNode import TrieNode

# Challenge 1: Total Number of Words in a Trie
# Approach: Iterate through child nodes using DFS (actually seemed to use a BFS) and increment word count when reaching end of word
# Could have used recursion to run in O(n) space complexity?
def total_words(root):
    word_count = 0
    if not root:
        return word_count
    stack = [root]
    while len(stack) > 0:
        # pop top of stack
        node = stack.pop(len(stack)-1)
        # push children to stack
        for child_node in node.children:
            if child_node:
                stack.append(child_node)
        if node.is_end_word:
            word_count += 1
    return word_count

# Challenge 2: Find All Words Stored in Trie
# Approach: DFS from root node adding all visited node values to a string, if we find an end node, append the string to an array and continue
def get_words(root, result, level, word):

    # Leaf denotes end of a word
    if root.is_end_word:
        # current word is stored till the 'level' in the character array
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(str(temp))

    for i in range(26):
        if root.children[i]:
            # Non-None child, so add that index to the character array
            word[level] = chr(i + ord('a'))  # Add character for the level
            get_words(root.children[i], result, level + 1, word)


def find_words(root):
    result = []
    word = [None] * 20  # assuming max level is 20
    get_words(root, result, 0, word)
    return result
 


# Challenge 3: List Sort Using Trie
# Approach: Construct a Trie from input list and then get words using Challenge 2 function
def sort_list(arr):
    trie = Trie()
    for word in arr:
        trie.insert(word)
    sorted = find_words(trie.root)
    return sorted

# Challenge 4: Word Formation From a Dictionary Using Trie
# Approach: Generate Trie from input list then iterate through the target word by querying next node in the trie until we can no longer do so (child node is null),
# next start from the root and query from the index that we stopped at
def is_formation_possible(dictionary, word):
    num_words_to_check = 2
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    
    # Keep track of where we are in the query word
    word_index = 0
    for i in range(num_words_to_check):
        # Start the search at root of trie
        node = trie.root
        last_node_was_end = False
        # iterate through word until we cannot find the next letter in the Trie
        while node:
            last_node_was_end = node.is_end_word
            char = word[word_index]
            node = node.children[ord(char) - ord('a')]
            if node:
                word_index += 1
                if word_index >= len(word)-1:
                    if node.is_end_word:
                        return True
            else:
                if not last_node_was_end:
                    return False
    return True
    
    
    



