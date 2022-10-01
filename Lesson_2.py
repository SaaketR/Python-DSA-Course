'''
Lesson 2 - Binary Search Trees, Traversals, and Recursion

Question:
    As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure to manage profile 
    information (username, name and email) for 100 million users. It should allow the following operations to be performed 
    efficiently:
        i. Insert the profile information for a new user.
        ii. Find the profile information of a user, given their username
        iii. Update the profile information of a user, given their username
        iv. List all the users of the platform, sorted by username
    You can assume that usernames are unique.

Interpretation of the Question:
    Create a data structure to store the profile information of 100 million users and be able to insert, find, update, and 
    list all the users/user information on the platform. All usernames are unique.

'''

# Building a framework for each user to store their username, name, and email:

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self):     # Object representation in string format, useful for debugging or constructing an object again
        return "User(username = '{}', name = '{}', email = '{}')".format(self.username, self.name, self.email)
    
    def __str__(self):      # String representation of object, useful for reprsenting code that is readable to customers
        return self.__repr__

# Building the database:

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert_user(self, user):        # Time = O(N), Space = O(1)
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:      # Check in self.users = [] for a username which is greater than the new user's username (user.username)
                break
            i += 1
        self.users.insert(i, user)      # Insert the user at self.users[i]

    def find_user(self, username):      # Time = O(N), Space = O(1)
        for user in self.users:     # Step through all the users
            if user.username == username:       # condition where the username matches
                return user

    def update_user(self, user):        # Time = O(N), Space = O(1)
        target = self.find_user(user.username)      # Use find_user() function to find a particular user and assign it to target
        target.name = user.name         # Updating the name of the target user
        target.email = user.email       # Updating the email of the target user

    def list_all_users(self):       # Time = O(1), Space = O(1)
        return self.users

# Sample Inputs (Users):

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

all_users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

database = UserDatabase()
database.insert_user(hemanth)
database.insert_user(biraj)
database.insert_user(siddhant)

# Building a Binary Tree

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left, self.right = None, None
    
    def parse_tuple(data):
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        return node

    def tree_to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.tree_to_tuple(self.left), self.key, TreeNode.tree_to_tuple(self.right)

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)
    
    def traverse_in(self):
        if self is None:
            return []
        return (TreeNode.traverse_in(self.left) + [self.key] + TreeNode.traverse_in(self.right))

    def traverse_pre(self):
        if self is None:
            return []
        return ([self.key] + TreeNode.traverse_pre(self.left) + TreeNode.traverse_pre(self.right))

    def traverse_post(self):
        if self is None:
            return []
        return (TreeNode.traverse_post(self.left) + TreeNode.traverse_post(self.right) + [self.key])

    def __repr__(self):
        return "Binary Tree <{}>".format(self.tree_to_tuple())
    
    def __str__(self):
        return "Binary Tree <{}>".format(self.tree_to_tuple())

# Building a Binary Search Tree

class BSTNode():
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.left, self.parent, self.right = None, None, None

'''
Binary Tree Operations:
    i.      Parsing a Tree Tuple    = converting tuple into a binary tree
    ii.     tree_to_tuple           = converting a binary tree into a tree tuple
    iii.    In-Order Traversal      = node.left, node.key, node.right
    iv.     Pre-Order Traversal     = node.key, node.left, node.right
    v.      Post-Order Traversal    = node.left, node.right, node.key
    vi.     Height/Depth of Tree    = length of longest path from root node to leaf
    vi.     Size of Binary Tree     = number of nodes in a binary tree
    vii.    Check if Binary Tree is a Binary Search Tree and return minimum and maximum key values 
    (bonus leetcode problems)
    vii.    Maximum depth of Tree
    viii.   Minimum depth of Tree
    ix.     Diamater of Binary Tree
'''

def parse_tuple(data):      # Converting a Tree Tuple into a Binary Tree
    if isinstance(data, tuple) and len(data) == 3:      # condition when data is a tuple of length 3
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])        # parsing left node
        node.right = parse_tuple(data[2])       # parsing right node
    elif data == None:      # condition when the data being parsed is no longer a tuple and is a None value (key is None type)
        node = None
    else:                   # condition when the data being parse is no longer a tuple and is an integer number now
        node = TreeNode(data)
    return node

def tree_to_tuple(tree):        # Converting a Binary Tree into a Tree Tuple
    pass

def InOrder_traversal(node):        # In Order Traversal of a Binary Tree
    if node is None:
        return []
    return (InOrder_traversal(node.left) + [node.key] + InOrder_traversal(node.right))

def PreOrder_traversal(node):       # Pre Order Traversal of a Binary Tree
    if node is None:
        return []
    return ([node.key] + PreOrder_traversal(node.left) + PreOrder_traversal(node.right))

def PostOrder_Traversal(node):      # Post Order Traversal of a Binary Tree
    if node is None:
        return []
    return (PostOrder_Traversal(node.left) + PostOrder_Traversal(node.right) + [node.key])

def height_bt(node):        # Finding the height of a Binary Tree
    if node is None:
        return 0
    return 1 + max(height_bt(node.left), height_bt(node.right))     # we only consider the longest side, hence take the max of heights of either sides

def size_bt(node):      # Finding the size of a binary tree
    if node is None:
        return 0
    return 1 + size_bt(node.left) + size_bt(node.right)     # counting nodes on both sides recursively

def is_bst(node):       # Checking if BT is a BST and returning Minimum and Maximum key values
    def remove_none(nums):
        return [x for x in nums if x is not None]
    
    if node is None:
        return True, None, None     # None node is a BST
    
    is_bst_l, min_l, max_l = is_bst(node.left)      # Evaluates is_bst() for the left sub-tree
    is_bst_r, min_r, max_r = is_bst(node.right)     # Evaluates is_bst() for the right sub-tree

    is_bst_node = (is_bst_l and is_bst_r and                        # Left sub-tree and right sub-tree are balanced
                    (max_l is None or node.key > max_l) and         # Left sub-tree contains nodes with keys less than node's keys
                    (min_r is None or node.key < min_r))            # Right sub-tree contains nodes with keys greater than node's keys
    
    min_key = min(remove_none([min_l, node.key, min_r]))        # Evaluating the minimum key on left sub-tree, node, and right sub-tree
    max_key = max(remove_none([max_l, node.key, max_r]))        # Evaluating the maximum key on left sub-tree, node, and right sub-tree

    return is_bst_node, min_key, max_key
    