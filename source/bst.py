import collections
class Node:

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

    def two_childre(self):
        """returns true if node has 2 children"""
        return self.right is not None and self.left is not None

    def height(self):
        """returns height of longest path to leaf from node"""
        # get  height of left path down tree if their else make -1
        left_height = self.left.height() if self.left is not None else -1
        # same as above but for right path down tree
        right_height = self.right.height() if self.right is not None else -1
        # return the greater of the two paths down tree +1 (accounting for og node)
        return 1 + max(right_height, left_height)



