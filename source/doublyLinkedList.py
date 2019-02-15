class Node:
  """ Node class for a doubly linked list """
  def __init__(self, data):
    """Initiates new instance of Node for doubly linked list """
    self.data = data
    self.next = None  # Sets the next pointer to None by default
    self.prev = None  # same as above but for prev pointer
  
  def __repre__(self):
    """ returns string representation of node """
  
class DoublyLinkedList:
  """ doubly linked list class """
  def __init__(self, items=None):
    """ initiates new instance of doubly linked list class """
    self.head = None  # sets a pointer to first node in list
    self.tail = None  # sets a pointer to last node in list 
    self.size = 0 # adds a size counter to keep length method constant time

    if items is not None: # if initiated with items
      for item in items:
        self.append(item) #  append them to linked list
  
  def __str__(self):
    """ returns formatted string of linked list when printed """
    items = ['({!r})'.format(item) for item in self.items()]
    return '[{}]'.format(' -> '.join(items))
  
  def __repr__(self):
        """Return a string representation of this linked list."""
        return 'DoublyLinkedList({!r})'.format(self.items())
  
  def items(self):
    """ returns python list of all items in dobuly linked list """
    items = []  # list of items to be returned
    cur = self.head # grab first node in linked list 
    while cur is not None:  # loop while node isnt nothing
      items.append(cur.data)  # append to items to be returned
      cur = cur.next  # grab the next node
    return items
  
  def is_empty(self):
    """ returns bool on whether the linked list is empty or not """
    return self.head is None  # returns true if self.head = empty
  
  def length(self):
    """ returns number of items in linked list """
    return self.size
  
  def append(self, item):
    """ inserts node to the end of linked list """
    new_node = Node(item) # create new node with item as data
    self.size += 1  # increments size of list
    cur_last = self.tail  # grab current last node in list
    self.tail = new_node  # point the tail to the new node 
    cur_last.next = new_node  # set current last node's next pointer towards new node
    new_node.prev = cur_last  # set the new nodes previous pointer to previous last node
  
  def prepend(self, item):
    """ inserts new node at the begenning of linked list """
    new_node = Node(item) # create new node with item as data
    self.size += 1  # increment size counter 
    cur_head = self.head  # grab current first node
    self.head = new_node  # point head pointer towards new node
    cur_head.prev = new_node  # set cur_head's previous pointer towards new node
    new_node.next = cur_head  # set new node's next pointer towards the previous cur_head

  

  
