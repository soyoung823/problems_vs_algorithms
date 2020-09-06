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


# Represents a single node in the Trie
class TrieNode:
    def __init__(self, value=''):
        ## Initialize this node in the Trie
        self.value = value
        self.next = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        # dictionary.get(keyname, value)
        # keyname: Required. The keyname of the item you want to return the value from
        # value: Optional. A value to return if the specified key does not exist. Default value None
        self.next[char] = self.next.get(char, TrieNode(char))
        

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffix_list = []
        for value in self.next:
            if self.next[value].next:
                suffix_list.extend(self.next[value].suffixes(suffix + value))
            elif value == '\x00':
                suffix_list.append(suffix)
        return suffix_list
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        cur_node = self.root

        for char in word:
            if char not in cur_node.next:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.next[char]

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        cur_node = self.root

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


'''

## Represents a single node in the Trie
class TrieNode:
    def __init__(self, value=""):
        # Initialize this node in the Trie
        self.value = value
        self.next = {}

    def insert(self, char):
        # Add a child node in this Trie
        self.next[char] = self.next.get(char, TrieNode(char))

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        suffix_list = []
        for value in self.next:
            if self.next[values].next:
                suffix_list.extend(self.next[value].suffixes(suffix + value))
            elif values == '\x00':
                suffix_list.append(suffix)
        return suffix_list

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root_node = {}

    def insert(self, word):
        # Add a word to the Trie
        word = word
        self.root_node[word[0]] = self.root_node.get(word[0], TrieNode(word[0]))
        current_node = self.root_node[word[0]]
        for i in range(1, len(word)):
            current_node.insert(word[i])
            current_node = current_node.next[word[i]]

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        cur_node = self.root

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

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');