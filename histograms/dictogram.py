import re, random, string, sys

class Dictogram(dict):
  ''' Dictogram is a histogram implemented as a subclass of dict class '''

  def __init__(self, text=None):
    ''' initialize a new dictogram with a string of text '''
    super(Dictogram, self).__init__() # initializes as a new dict 
    # **Add properties Tokens and Types to easily reference uniques and all words**
    self.types = 0  # Types are unique words
    self.tokens = 0 # Tokens are appearances of words (total_words)
    # * count words in the given text
    if text is not None:
      pass #! Need to make a clean_up_text method to string what i need

  def add_to_count(self, word):
    ''' Checks if word is in dictogram and either adds it or adds to frequency count '''
    self.tokens += 1
    if word in self:
      self[word] += 1
    else:
      self[word] = 1
      self.types += 1
    
  def frequency(self, word):
    ''' Checks frequency of word in dictogram '''
    if word in self:
      return self[word]
    else:
      return 0
  
  
