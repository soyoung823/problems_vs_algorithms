TrieNode:
when n is the number of nodes in the Trie.

Time complexity: 
    insert: O(1) since the procedure uses a constant time dictionary insertion.
    
    suffixes: O(n) since we visit every node once each at worst case. 

Trie:
Time complexity:
    insert: O(m) when m is the length of word.

    find: O(m) when m is the length of prefix.

space complexity:
    O(n) when n is the number of nodes in Trie. 
