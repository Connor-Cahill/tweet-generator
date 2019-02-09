import string

class Histogram:
  ''' histogram class holds methods used accross all implementations '''
  
  def __init__(self, file=None):
    self.tokens = 0
    self.types = 0

  def create_text(self, file):
    ''' Takes in file and returns list of lower case, puncaution stripped text '''
    with open(file) as word_file:
      text = word_file.read()
      new_text = text.lower()
      translator = str.maketrans('', '', string.punctuation)
      new_text = new_text.translate(translator)
    words = [word for line in new_text.split('\n') for word in line.split(' ')]
    return words

  def unique_words(self):
    ''' Returns count of unique words in histogram '''
    return self.types
  
  def word_count(self):
    ''' Returns total word count in histogram '''
    return self.tokens
  