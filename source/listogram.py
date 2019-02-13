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
      # words = self.create_text(file)  ## method is part of histogram class
      for word in file:
        self.add_count(word)
  
  def add_count(self, word, count=1):
    ''' given words either adds to frequency or adds word in listogram '''
    self.tokens += count
    for lst in self:
      if lst[0] == word:
        lst[1] += count
        return
    self.append([word, count]) # if word not in list, append an inner list for word
    self.types += 1

  def frequency(self, word):
    ''' returns the frequency of a word in a listogram '''
    for lst in self:
      if lst[0] == word:
        return lst[1] ## lst[1] hold freq value
    return 0
  
  def __contains__(self, word):
    """ Returns bool whether word is in listogram """
    for lst in self:
      if lst[0] == word:
        return True
    return False
  
  def _index(self, target):
    """ Takes a target word and returns index # """
    for i, lst in enumerate(self):
      if lst[0] == target:
        return i

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
    return self

  def to_file(self, file):
    """Takes listogram and writes it to file """
    with open(file, 'w') as write_file:
      for i in range(len(self)):
        write_file.write('Type: {}, Tokens: {}\n'.format(self[i][0], self[i][1]))



def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
  ''' Runs some test stuff on listogram class '''
  file = sys.argv[1]
  my_listo = Listogram(file)
  sorted_listo = my_listo.sort_listogram()
  my_listo.to_file('test.txt')
  # print(sorted_listo)


if __name__ == '__main__':
  main()

  



  
    
  
