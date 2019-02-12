import sys
from listogram import Listogram

'''
Note About Tupleagram Class:
----------------------------
It inherits all methods from Listogram/Histogram classes. 
Only thing overridden from Listogram class was the add_to method,
everything else functions as is
'''

class Tupleagram(Listogram):
  """ Histogram Implemented list of tuples """
  def __init__(self, file=None):
    """Initaliazes new tupleagram """
    super(Tupleagram, self).__init__() # inits new instance of tupleagram
    #* Add type/token count to keep those methods to O(1)
    self.types = 0
    self.tokens = 0
    #* if file not empty create tupleagram with file
    if file is not None:
      # words = self.create_text(file)
      for word in file:
        self.add_count(word)
    
  #* NOTE: this method was overridden to work with appending tuples instead of lists
  def add_count(self, word, count=1):
    """Takes a word and adds to tupleagram or frequency if word in tupleagram """
    self.tokens += count # add to token count with every word given
    for i, tup in enumerate(self):
      if word == tup[0]:
        num = tup[1] + count
        self.pop(i)
        self.append((word, num)) # increment previous val of num 
        return
    self.types += 1 # add types count if unique word
    self.append((word, count))


def test_repeats(tupleagram):
  """ Takes in tupleagram and tests to make sure types are duplicated """
  for i in range(len(tupleagram)):
    for j in range(len(tupleagram)):
      if tupleagram[i][0] == tupleagram[j][0] and i != j:
        print('ERROR: There are duplicate types in tupleagram!')
        return
  print('All good')
    

def main():
  ''' Runs some test stuff on tupleagram class '''
  file = sys.argv[1]
  my_tup = Tupleagram(file)
  sorted_tup = my_tup.sort_listogram()  ## Using sort_listogram from listogram class
  # my_tup.to_file('test.txt')
  # print(sorted_tup)
  test_repeats(my_tup)


if __name__ == '__main__':
  main()