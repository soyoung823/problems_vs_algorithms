from collections import defaultdict

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class TrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = defaultdict(TrieNode)
        self.handler = handler

    def insert(self, path_part):
        # Insert the node as before
        self.children[path_part] = TrieNode()


# A RouteTrie will store our routes and their associated handlers
class Trie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = TrieNode(handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for path_part in path:
            # if path_part not in node.children:
            node.insert(path_part)
            node = node.children[path_part]   
        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Find the trie node that represents this path
        # Return the handler for a match, or None for no match
        node = self.root
        for path_part in path:
            if path_part not in node.children:
                return None
            node = node.children[path_part]
        return node.handler


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = Trie(handler)
        self.not_found_hanlder = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        # node = self.routeTrie
        path_list = self.split_path(path)
        self.routeTrie.insert(path_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        found = self.routeTrie.find(path_list)
        if found is None:
            return self.not_found_hanlder
        return found

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path = path.strip('/')
        #return path.split('/') if path else []
        if path:
            return path.split('/')
        return []


# Test Cases
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler", ) # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("")) # should print 'root handler'
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one