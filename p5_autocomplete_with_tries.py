'''
Building a Trie in Python
Before we start let us reiterate the key components of a Trie or Prefix Tree. 
A trie is a tree-like data structure that stores a dynamic set of strings. 
Tries are commonly used to facilitate operations like predictive text or 
autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings. 
We will create two classes:

A Trie class that contains the root node (empty string)
A TrieNode class that exposes the general functionality of the Trie, 
like inserting a word or finding the node which represents a prefix.
Give it a try by implementing the TrieNode and Trie classes below!
'''

## Represents a single node in the Trie
class TrieNode:
    def __init__(self, value=None):
        # Initialize this node in the Trie
        self.value = value
        self.children = {}
        self.is_end = False

    def insert(self, char):
        # Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode(char)

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        suffix_list = []
        for char in self.children:
            node = self.children[char]
            if node.is_end:
                suffix_list.append(suffix + node.value) 
            if node.children:
                suffix_list.extend(node.suffixes(suffix + node.value))

        return suffix_list

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root_node = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        cur_node = self.root_node
        for char in word:
            cur_node.insert(char)
            cur_node = cur_node.children[char]
        cur_node.is_end = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if not prefix:
            return self.root_node

        cur_node = self.root_node
        for char in prefix:
            if char not in cur_node.children:
                return None
            cur_node = cur_node.children[char]
        return cur_node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print(MyTrie.find("ant").value)
print(MyTrie.find("ant").is_end)
print(MyTrie.find("anth").value)
print(MyTrie.find("anth").is_end)

print(MyTrie.find('an').suffixes())
print(MyTrie.find('f').suffixes())