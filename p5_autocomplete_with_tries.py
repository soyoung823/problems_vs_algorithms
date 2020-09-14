'''
Trie class: contains the root node ('')
TrieNode class: generates Trie with TrieNode, inserts a word, find the node representing a prefix 
'''
## Represents a single TrieNode in the Trie
class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.is_end = False

    def insert(self, character):
        if character not in self.children:
            self.children[character] = TrieNode(character)

    def suffixes(self, suffix=''):
        suffix_list = []
        sub_list = []
        for character in self.children:
            node = self.children[character]
            if node.is_end:
                sub_list.append(suffix + node.value)
                suffix_list.extend(sub_list)
            
            if node.children:
                suffix_list.extend(node.suffixes(suffix + node.value))

        return suffix_list

## Trie class containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root_node = TrieNode()

    def insert(self, word):
        current_node = self.root_node
        for character in word:
            current_node.insert(character)
            current_node = current_node.children[character]
        current_node.is_end = True

    def find(self, prefix):
        if not prefix:
            return self.root_node

        current_node = self.root_node
        for character in prefix:
            if character not in current_node.children:
                return None
            current_node = current_node.children[character]
        return current_node

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
print(MyTrie.find('f').value)
print(MyTrie.find('f').suffixes())