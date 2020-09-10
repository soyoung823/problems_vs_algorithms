1. Problem explanations
The goal is to implement a HTTP Router using a Trie like we would find in a typical web server.
Trie will contain a part of the http path at each node, building from the root node /.

We will print out to ensure we got the right handler.
We will split the path by '/' slashes.
We will need to insert and find nodes and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.

2. Complexity explanations
Time and Space complexity:
TrieNode: 
    insert 
    Time: O(1) since it inserts a TrieNode()
    Space: O(n) since a new TrieNode is created and inserted

Trie:
    insert: O(n) since it uses a for loop to interate each path_part.
    Space: O(1) since it doesn't use any auxiliary space.

    find: 
    Time: O(n) since it uses a for loop to interate each path_part.
    Space: O(1) since it doesn't use any auxiliary space.

Router:
    add_handler: 
    Time: O(n) since it uses an insert method which iterates each path_part.
    Space: O(n) since a new TrieNode is created and inserted for eaach path_part.

    lookup: 
    Time: O(n) since it uses a find method which iterates each path_part.
    Space: O(1) since it doesn't use any auxiliary space.
