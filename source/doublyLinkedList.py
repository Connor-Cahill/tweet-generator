from linkedList import LinkedList, Node

class DoublyNode(Node):
  """ Node class for a doubly linked list """
  def __init__(self, data):
    """Initiates new instance of Node for doubly linked list """
    self.data = data
    self.next = None  # Sets the next pointer to None by default
    self.prev = None  # same as above but for prev pointer
  
  def __repre__(self):
    """ returns string representation of node """
  
class DoublyLinkedList(LinkedList):
  """ doubly linked list class """
  def __init__(self, items=None):
    """ initiates new instance of doubly linked list class """
    self.head = None  # sets a pointer to first node in list
    self.tail = None  # sets a pointer to last node in list 
    self.size = 0 # adds a size counter to keep length method constant time

    if items is not None: # if initiated with items
      for item in items:
        self.append(item) #  append them to linked list

  def append(self, item):
    """ inserts node to the end of linked list """
    new_node = DoublyNode(item) # create new node with item as data
    if self.is_empty(): # check if list is empty 
      self.tail = new_node  # set tail pointer towards new node
      self.head = new_node  # same as above but with head pointer
      self.size += 1  # increment size
      return  # break method
    self.size += 1  # increments size of list
    cur_last = self.tail  # grab current last node in list
    self.tail = new_node  # point the tail to the new node 
    cur_last.next = new_node  # set current last node's next pointer towards new node
    new_node.prev = cur_last  # set the new nodes previous pointer to previous last node
  
  def prepend(self, item):
    """ inserts new node at the begenning of linked list """
    new_node = DoublyNode(item) # create new node with item as data
    if self.is_empty(): # check if list is empty 
      self.head = new_node  # if empty set head pointer to new_node
      self.tail = new_node  # same as above but with tail pointer
      self.size += 1  # increment size
      return  # break method
    self.size += 1  # increment size counter 
    cur_head = self.head  # grab current first node
    self.head = new_node  # point head pointer towards new node
    cur_head.prev = new_node  # set cur_head's previous pointer towards new node
    new_node.next = cur_head  # set new node's next pointer towards the previous cur_head
  
  def delete(self, item):
    """ deletes an item from linked list """
    if self.head is None and self.tail is None: # check if linked list is empty
      raise ValueError('List is empty') # if yes, throw error
    if item == self.head.data: # If item is the head
      if self.head.next is not None:  # check if head's next node is empty or not
        self.head = self.head.next # Set head to be next item
        self.head.prev = None # Set new head's previous to be None
      else: # If self.head.next is None : empty list
        self.head = None  # clear head
        self.tail = None  # clear tail
        self.size = 0 # reset counter
      return  # break function
    cur_node = self.head.next # grab value of node to start looping
    while cur_node is not None: # while node is not None
      if cur_node.data == item: # if current node's data is item
        if cur_node is not self.tail: # check if cur_n
          cur_node.next.prev = cur_node.prev # grab next node in list
          prev.next = next_node # setting the next pointer of previous node to next_node
        else:
          self.tail = cur_node.prev
        self.size -= 1  # decrement size counter
        return
      cur_node = cur_node.next  # grab next node in list
    raise ValueError('Item not found: {}'.format(item)) # Value not in linked list. throws an error

def test_list():
  """ runs test methods on the doubly linked list class """
  ll = DoublyLinkedList()
  ll.append('Cat')
  print(ll)
  ll.prepend('yellow')
  ll.append('pink')
  print(ll)
  print('HEAD', ll.head)
  print('TAIL', ll.tail)
  ll.delete('yellow')
  print(ll)
  print(ll.head)
  print(ll.tail)
  ll.delete('Cat')
  ll.delete('pink')
  print(ll)
  print(ll.head)
  print(ll.tail)



  


if __name__ == "__main__":
  test_list()






  
