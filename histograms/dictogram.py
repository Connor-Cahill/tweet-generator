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
      words = self.clean_up_text(text)
      for word in words:
        self.add_to_count(word)
    

  def add_to_count(self, word):
    ''' Checks if word is in dictogram and either adds it or adds to frequency count '''
    self.tokens += 1
    print('Something is happening i promise')
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
  
  def clean_up_text(self, text):
    ''' Texts in text and removes special chars and newlines for dictogram '''
    new_text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    ret = new_text.translate(translator)
    ret = ret.split(' ')
    return ret
  

  def to_file(self, file):
    ''' Takes dictogram and writes it to inputted file '''
    with open(file, 'w+') as text_file:
      text_file.write('\n****** NEW HISTOGRAM RESULTS *******\n')
      for key, value in self.items():
        text_file.write('{} : {}\n'.format(key, value))




def main():
  ''' runs some testing for Dictogram class '''
  file = sys.argv[1]

  my_dict = Dictogram(file)

  my_dict.to_file('dicto_results.txt')


if __name__ == "__main__":
  main()


