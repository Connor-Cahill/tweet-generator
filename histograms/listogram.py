import sys

from histogram import Histogram

class Listogram(list, Histogram):
  ''' Histogram Implemented with list of lists '''
  def __init__(self, file=None):
    ''' Initializes new listogram instance '''
    super(Listogram, self).__init__() ## inits new instance of listogram (list)
    #* Add type/token count to keep those methods to O(1)
    self.types = 0
    self.tokens = 0
    #* If file is not empty, create listogram
    if file is not None:
      words = self.create_text(file)  ## method is part of histogram class
      for word in words:
        if len(self) == 0:
          self.append([word, 1])
        for lst in self:
          self.add_to(lst, word)
  
  def add_to(self, lst, word):
    ''' given words either adds to frequency or adds word in listogram '''
    self.tokens += 1
    if lst[0] == word:
      lst[1] += 1
    else:
      self.append([word, 1]) # if word not in list, append an inner list for word
      self.types += 1

  def frequency(self, word):
    ''' returns the frequency of a word in a listogram '''
    for lst in self:
      if lst[0] == word:
        return lst[1] ## lst[1] hold freq value
      else:
        print('Word not in listogram');

  def print_listogram(self):
    for lst in self:
      print('Type: {} - Tokens: {}'.format(lst[0], lst[1]))
  
  def sort_listogram(self):
    ''' Takes in listogram as input and sorts it by frequency '''
    for i in range(len(self)):
      for j in range(len(self)):
        # checking the freq value in listogram (comparing)
        if self[j][1] > self[i][1]:
          self[j], self[i] = self[i], self[j]

def main():
  ''' Runs some test stuff on listogram class '''
  file = sys.argv[1]
  my_listo = Listogram(file)
  print(my_listo)


if __name__ == '__main__':
  main()

  



  
    
  
