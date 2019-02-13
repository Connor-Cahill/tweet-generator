import re, random, string, sys
from histogram import Histogram

class Dictogram(dict, Histogram):
  ''' Dictogram is a histogram implemented as a subclass of dict class '''

  def __init__(self, file=None):
    ''' initialize a new dictogram with a string of text '''
    super(Dictogram, self).__init__() # initializes as a new dict 
    # **Add properties Tokens and Types to easily reference uniques and all words**
    self.types = 0 # Types are unique words
    self.tokens = 0 # Tokens are appearances of words (total_words)
    # * count words in the given text
    ## NOTE: if working with a file instead of list you can use self.create_text() method
    if file is not None:
      for word in file:
        self.add_count(word)

    

  def add_count(self, word, count=1):
    ''' Checks if word is in dictogram and either adds it or adds to frequency count '''
    self.tokens += count
    if word in self:
      self[word] += count
    else:
      self.types += 1
      self[word] = count
      
    
  def frequency(self, word):
    ''' Checks frequency of word in dictogram '''
    if word in self:
      return self[word]
    else:
      return 0
  

  def to_file(self, file):
    ''' Takes dictogram and writes it to inputted file '''
    with open(file, 'w+') as text_file:
      text_file.write('\n****** NEW HISTOGRAM RESULTS *******\n')
      for key, value in self.items():
        text_file.write('{} : {}\n'.format(key, value))

  def print_dictogram(self):
    ''' Prints the dictograms types and tokens to terminal '''
    for types, tokens in self.items():
      print('Type: {} - Tokens: {}'.format(types, tokens))
  
  def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a dictogram and display its contents
    histogram = Dictogram(word_list)
    print('dictogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    

def main():
  ''' runs some testing for Dictogram class '''
  file = sys.argv[1]
  my_dict = Dictogram(file)
  my_dict.print_dictogram()
  print(my_dict)
  print(my_dict['of'])


if __name__ == "__main__":
  main()


