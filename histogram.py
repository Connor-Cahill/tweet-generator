

def histogram(file):
  '''
  Takes file as argument, reads file and counts word frequency stores freq in dict. returns a dictionary
  '''
  word_freq = {}
  word_file = open(file, 'r').read()
  word_arr = word_file.split(' ')
  for word in word_arr:
    if word in word_freq:
      word_freq[word] += 1
    else:
      word_freq[word] = 1
  return word_freq

def unique_words(hist):
  '''
  Given a histogram returns total count of unique words (returns Int)
  '''
  return len(hist.keys)

def frequency(word, hist):
  '''
  Given a word as input returns frequency of word (reads from histogram)
  '''
  return hist[word]


if __name__ == '__main__':
  my_dict = histogram(input('Please input a file name: '))
  print(my_dict)
