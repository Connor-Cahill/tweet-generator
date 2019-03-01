import collections


class BinaryTreeNode:

    def __init__(self, data):
        """Creates new instance of binary search tree node"""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """prints string representation of binary tree node"""
        return 'Node({})'

    def is_leaf(self):
        """return true if a node has no children"""
        return self.left is None and self.right is None

    def is_branch(self):
        """returns true if node has at least 1 child"""
        return self.left is not None or self.right is not None

    def two_children(self):
        """returns true if node has 2 children"""
        return self.right is not None and self.left is not None

    def height(self):
        """returns height of longest path to leaf from node"""
        # get  height of left path down tree if their else make -1
        left_height = self.left.height() if self.left is not None else -1
        # same as above but for right path down tree
        right_height = self.right.height() if self.right is not None else -1
        # return the greater of the two paths down tree +1
        return 1 + max(right_height, left_height)


class BinarySearchTree:

    def __init__(self, items=None):
        """creates a new instance of a binary search tree"""
        self.root = None  # top node in bst 
        self.size = 0  # number of nodes in bst
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """return a string representation of binary search tree"""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """return true if this binary tree is empty"""
        return self.root is None  # Empty!

    def height(self):
        """returns height of longest path from root node to leaf in bst"""
        if self.is_empty():
            return 0  # tree is empty, length 0
        # find height from root node. Add 1 to account for root
        return self.root.height() + 1

    def contains(self, item):
        """returns true if item is in tree"""
        # find item using find method, assign to node var
        node = self._find_node_recursive(item, self.root)
        return node is not None  # true if node is there

    def search(self, item):
        """return item matching inputted item in tree"""
        # find node matching given item
        node = self._find_node_recursive(item, self.root)
        return node.data if node is not None else None

    def insert(self, item):
        """insert the given item in correct spot in bst"""
        if self.is_empty():
            self.root = BinaryTreeNode(item)  # creates root node
            self.size += 1  # increment size counter
            return  # break out of function
        # find parent of where node should be
        parent = self._find_parent_recursive
        # check if item is less than parents data
        if item < parent.data:
            parent.left = BinaryTreeNode(item)
        # check if item is larger than parents data
        elif item > parent.data:
            parent.right = BinaryTreeNode(item)
        self.size += 1  # increment size counter

    def _find_node_iterative(self, item):
        """finds a node in a BST thats data matches the item"""
        node = self.root  # grab value of root node
        # loop while the node is there
        while node is not None:
            if node.data == item:
                return node  # node's data matches item, return node
            # check if item is less than nodes data
            elif item < node.data:
                node = node.left  # go left down tree
            # check if item is greater than node data
            elif item > node.data:
                node = node.right  # assend right down tree
        return None  # item is not in the tree

    def _find_node_recursive(self, item, node):
        """returns node from BST thats data matches inputted
           object, if not in BST returns None"""
        # check that node exists
        if node is None:
            return None  # Base case: Node not found
        # see if nodes data equals item
        elif node.data == item:
            return node  # return the node
        # check if item less than nodes data
        elif item < node.data:
            # call again with left child node
            return self._find_node_recursive(item, node.left) 
        # check if item less than
        elif item > node.data:
            # call again assending right down tree
            return self._find_node_recursive(item, node.right) 

    def _find_parent_node_iterative(self, item):
        """finds the parent node of a node thats data equals item"""
        node = self.root  # get starting node 
        parent = None  # parent set to none to start
        while node is not None:
            # check if the nodes data equals item
            if item == node.data:
                return parent
            parent = node  # assign parent as current node
            if item < node.data:  # if item larger than nodes data
                node = node.left  # go down left side of tree
            elif item > node.data:  # check if item larger
                node = node.right  # continue down right side of tree
        return parent  # returns None! 

    def _find_parent_node_recursive(self, item, node, parent=None):
        """returns parent node of node thats data matches item."""
        if node is None:
            # not found base case 
            return parent
        # check if item less than data
        elif item < node.data:
            # call func again with left child as node
            return self._find_parent_node_recursive(item, node.left, node)
        # check if item is larger
        elif item > node.data:
            # call func again with right child as node
            return self._find_parent_node_recursive(item, node.right, node)

    def delete(self, item):
        """remove item from tree if present"""
        node = self._find_node_recursive(item)
        # check if node is a leaf
        if node.is_leaf():
            # find parent of node
            parent = self._find_parent_node_recursive(node.data)
            if parent.left == node:  # check if node is parents left child
                parent.left = None  # remove it
                self.size -= 1  # decrement size conuter
                return
            elif parent.right == node:  # check if node is parents right child
                parent.right = None  # remove it 
                self.size -= 1  # decrement size counter
                return
            else:
                return None
        # check if node has 2 children
        elif node.two_children():
            pass

    def items_in_order(self):
        """return an in-order list of all items in bst"""
        items = []  # create empty arr for bst items 
        # make sure tree isn't empty 
        if not self.is_empty():
            # traverse tree in order from root, append each node
            self._traverse_in_order(self.root, items.append)
        return items  # return arr of items 

    def _traverse_in_order_recursive(self, node, visit):
        """traverse bst in order (DFS)"""
        # break when node is nothing 
        if node is not None:
            # call again with left child
            self._traverse_in_order_recursive(node.left, visit)
            # call visit on node
            visit(node.data)
            # call func again with right child
            self._traverse_in_order_recursive(node.right, visit)

    def items_pre_order(self):
        """return a pre-order arr of all items in BinarySearchTree"""
        items = []  # empty arr for items 
        if not self.is_empty():  # check if emtpy
            # traverse tree and append each item 
            self._traverse_pre_order_recursive(self.root, items.append)
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """traverse this bst pre-order DFS"""
        # make sure node is there
        if node is not None:
            # visit node
            visit(node.data)
            self._traverse_pre_order_recursive(self.left, visit)
            self._traverse_pre_order_recursive(self.right, visit)

    def items_post_order(self, node, visit):
        """returns items from bst post order"""
        items = []  # set empty arr for  items 
        if not self.is_empty():  # check if bst is empty
            # traverse the tree post order and append to items
            self._traverse_post_order_recursive(self, node, items.append)
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """traverse bst post order and vist each node"""
        if node is not None:  # make sure node is there
            # traverse down left side of tree
            self._traverse_post_order_recursive(node.left, visit)
            # traverse right side of tree
            self._traverse_post_order_recursive(node.right, visit)
            # call visit on node
            visit(node.data)

    def items_level_order(self):
        """return level order list of all items in bst"""
        items = []  # empty arr for items
        if not self.is_empty():  # make sure tree isnt empty
            # traverse level order from root appending each node to items
            self._traverse_level_order_iterative(self, self.root, items.append)
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """traverse bst with level-order traversal (BFS)"""
        q = collections.deque()  # create empty queue 
        q.append(start_node)  # append start node to queue
        while len(q) > 0:  # loop while queue is not empty
            node = q.popleft()  # pop item in queue
            visit(node.data)  # call visit on node
            if node.left is not None:  # check if left child
                q.append(node.left)  # append to queue
            if node.right is not None:  # check right child
                q.append(node.right)  # append right child

