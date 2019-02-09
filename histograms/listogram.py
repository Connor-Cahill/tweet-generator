
from histogram import Histogram

class Listogram(list, Histogram):
  ''' Histogram Implemented with list of lists '''

  def __init__(self, file=None)
  ''' Initializes new listogram instance '''
  super(Listogram, self).__init__() ## inits new instance of listogram (list)
  #* Add type/token count to keep those operators to O(1)
  self.types = 0
  self.tokens = 0
  #* If file is not empty, create listogram
  if file is not None:
    words = self.create_text(file)
    for word in words:
      self.add_to(word)
  
  def add_to(self, word):
    ''' given words either adds to frequency or adds word in listogram '''
    self.tokens += 1
    for lst in self:
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
  
  


  
    
  
