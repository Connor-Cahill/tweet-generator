import collections


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.left is None and self.right is None  #  returns true if node has no children

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return self.right is not None or self.left is not None

    def two_children(self):
        """ returns true if node has both children """
        return self.right is not None and self.left is not None

    def height(self):
        """returns height of longest path from node to leaf """
        # get height of left path down tree IF node is there, if not make -1
        left_height = self.left.height() if self.left is not None else -1
        #  same as above but for right path down tree 
        right_height = self.right.height() if self.right is not None else -1
        # returns the greater of the right and left heights + 1 
        return 1 + max(right_height, left_height)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self, node=None):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node)."""
        if self.is_empty():
            return 0  # if BST is empty return 0 
        return self.root.height() + 1  # else return height from root

    def contains(self, item):
        """Return True if this binary search tree contains the given item."""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found."""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        return node.data if node is not None else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree."""
        # Handle the case where the tree is empty
        if self.is_empty():
            self.root = BinaryTreeNode(item)  # create first node
            self.size += 1  # increment size counter 
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        if item < parent.data:  # if item is less than parents data
            parent.left = BinaryTreeNode(item)  # set it as left child
        elif item > parent.data:
            parent.right = BinaryTreeNode(item)  # if greater, set as right 
        self.size += 1  # increment size counter

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node."""
        node = self.root  # grab the first node (root)
        while node is not None:  # while node is something
            if node.data == item:  # if node's data is item
                return node  # return it
            elif item < node.data:  # if item less than data
                node = node.left  # set node = to node's left child (smaller)
            elif item > node.data:  # item greater than data
                node = node.right  # set node equal to right node (greater )
        return None  # item not in list

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        elif node.data == item:
            # Return the found node
            return node
        elif item < node.data:  # check if item is smaller than data
            return self._find_node_recursive(item, node.left)  # call again with left node (smaller value)
        elif item > node.data:  # check if item larger than data
            return self._find_node_recursive(item, node.right)  # call with right node, larger value

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node."""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        while node is not None:  # loop while node is something
            if item == node.data:  # if item = node data
                # Return the parent of the found node
                return parent
            elif item < node.data:  # if item smaller than node.data
                parent = node  # set parent to node
                node = node.left  # set node to left child
            elif item > node.data:  # if item greater 
                parent = node  # set parent to node 
                node = node.right  # set node to right child
            return parent  # returns none 

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        if item == node.data:
            # Return the parent of the found node
            return parent
        elif item < node.data:
            # set parent as the node and node as the left child (lesser)
            return self._find_parent_node_recursive(item, node.left, node)
        elif item > node.data:
            # set parent as the current node and node as the right child (greater)
            return self._find_parent_node_recursive(item, node.right, node)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError."""
        # based on how many children the node containing the given item has and
        pass
        node = self._find_node_recursive(item)
        # if node.is_leaf():
        #      parent = self._find_parent_node_recursive(node.data)
        # if parent.left == node:
        #     parent.left = None
        #     return
        # else:
        #     parent.right = None
        # elif node.two_children():
        #   pass

        # implement new helper methods for subtasks of the more complex cases

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
            # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function"""
        if node is not None:
            self._traverse_in_order_recursive(node.left, visit)
            visit(node.data)
            self._traverse_in_order_recursive(node.right, visit)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function."""
        if node is not None:
            visit(node.data)  # visit the node 
            # run func again with left child as node
            self._traverse_pre_order_recursive(node.left, visit)
            # run func again with right child as node
            self._traverse_pre_order_recursive(node.right, visit)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
            # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function."""
        if node is not None:
            # traverse down left side first
            self._traverse_post_order_recursive(node.left, visit)
            # traverse down right side nect 
            self._traverse_post_order_recursive(node.right, visit)
            # visit the node
            visit(node.data)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function."""
        queue = collections.deque()  # create a queue
        queue.append(start_node)  # put start node in queue
        while len(queue) > 0:  # loop while queue has something in it
            node = queue.popleft()  # pop left item and return 
            visit(node.data)  # visit removed node
            if node.left is not None:  # if left child append to queue
                queue.append(node.left)
            if node.right is not None:  # if right child append to queue
                queue.append(node.right)

