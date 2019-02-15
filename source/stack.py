from linkedList import Node

class Stack_Node(Node):
  """ node for the stack class """
  def __init__(self):
    """ creates new instance of Stack Node """
    self.data = None  # Data None by default
    self.next = None  # set next pointer to None by default

class Stack:
  """ linked list stack implementation """
  def __init__(self):
    """ creates new instance of stack """
    self.size = 0 # size counter for our stack (keeps length method constant time)
    self.head = None  # first node set to none by default 

  def is_empty(self):
    """ returns bool whether stack is empty """
    return self.head is None  # returns true if self.head is None

  def push(self, item):
    """ pushes new item onto stack """
    new_node = Stack_Node()  #  create new node 
    new_node.data = item  # set data of new node to item
    new_node.next = self.head # set new node's next pointer to the current head
    self.head = new_node  # reassign head pointer to our new node
    self.size += 1  # increment size counter by 1

  def pop(self):
    """ removes node from top of stack """
    if self.is_empty(): # check if stack is empty 
      return None #   if empty return none
    else:
      pop_item = self.head  # grab current head node
      self.head = pop_item.next # reassign head to old head's next node
      self.size -= 1  # decrement size counter
      return pop_item.data  # return data of popped item
    
  def peek(self):
    """ peek at data at top of stack """
    return self.head.data # return head data
  
  def length(self):
    """ returns size of stack """
    return self.size  # size of stack
  
  def __str__(self):
    """ prints string representation of stack """
    ret_string = '' # create return string
    node = self.head #  grab value of first node
    while node is not None: # loop while node is not node
      ret_string += '[ {} ]'.format(node.data) # append data to return string 
      node = node.next  # reassign node to next node in stack
    return ret_string

def test_stack():
  """ runs some test methods on a stack """
  stack = Stack()
  stack.push('A')
  stack.push('B')
  stack.push('C')
  print(stack)
  print('PEEK: ', stack.peek())
  print('POP: ', stack.pop())
  print(stack.head.data)


if __name__ == "__main__":
  test_stack()


  




