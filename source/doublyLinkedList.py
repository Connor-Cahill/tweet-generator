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
