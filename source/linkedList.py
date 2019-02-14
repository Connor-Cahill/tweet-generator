class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(1) because we made size a property of the linked list class"""
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) because we have the tail pointer and just need to readjust 2 pointers"""
        new_node = Node(item) # Creates new node
        self.size += 1 #  increment size of linkedlist counter
        cur_last = self.tail  # stores value of current tail to cur_val
        self.tail = new_node  # changes the tail to the new_node
        if cur_last is not None:
          cur_last.next = new_node  # adds the new_node to the cur_lasts next pointer
        if self.head is None:
          self.head = new_node

        

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Because we have a head pointer so we only need to adjust 2 pointers"""
        new_node = Node(item) # create new node
        self.size += 1 #  increment size of linked list counter
        next_node = self.head # gets value of current first and stores as next_node
        self.head = new_node  # sets the new_node as the head
        print(self.head)
        new_node.next = next_node # sets the new_node's pointer towards the previous head (next_node)
        if self.tail is None:
          self.tail = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) if the quality is the head or tail nodes data
        TODO: Worst case running time: O(n) we have to loop through every node"""
        if self.head.data == quality: # Check if the head node's data is what we are looking for 
          return self.head.data # if it is return it and break the function
        if self.tail.data == quality: # Same as above but checking tail pointer
          return self.tail.data
        cur_node = self.head
        while cur_node is not None:
          if quality(cur_node.data):
            return cur_node.data
          cur_node = cur_node.next
        return None

        current_node = self.head  # Assign first node to current_node var
        while current_node is not None:  # loop through linkedList while current node's next pointer is not None
          if current_node.data == quality:  # if current nodes data equals quality, return it
            return current_node.data
          current_node = current_node.next  # reassinging current_node to the next node in linked list
        return None #! What am I supposed to do? What is this methods purpose?

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) If item is head node's data
        TODO: Worst case running time: O(n) we have to loop through all nodes"""
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if self.is_empty():
          raise ValueError('Item not found: {}'.format(item))
        if item == self.head.data:
          cur = self.head
          self.head = cur.next # assigning head to the current head node's next
          self.size -= 1 #  decrement linked list size property
          return  # break func O(1)
        prev_node = self.head
        cur_node = self.head.next # assign 2nd node in linked list to cur_node
        while cur_node is not None:  # iterate through linked list while cur node is not none
          print(self)
          if cur_node.data == item: # if cur_node's data = item:
            if cur_node == self.tail:
              self.tail = prev_node
            prev_node.next = cur_node.next #  assign pointer of previous to pointer of current_node's next 
            self.size -= 1  # decrement size property of linked list
            return  # break da function
          prev_node = cur_node  # update previous node to = cur_node
          cur_node = cur_node.next  # get cur_node's next and set to cur_node
        raise ValueError('Item not found: {}'.format(item)) # Value not in linked list. throws an error






def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
    # ll = LinkedList()
    # ll.prepend('purple')
