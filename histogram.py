import re

##histogram list of tuples implementation
def histogram(file):
  '''
  Takes file as argument, reads file and counts word frequency stores freq in dict. returns a dictionary
  '''
  histogram = []
  text = open(file, 'r').read()
  words = [word for line in text.split('\n') for word in line.split(' ')]
  for word in words:
    add_word_to_histogram(histogram, word)
  return histogram


def add_word_to_histogram(histogram, word):
  '''
  Adds a word or freq to tuple in histogram list
  '''
  for i in range(len(histogram)):
    if histogram[i][0] == word:
      histogram[i] = (word, histogram[i][1] + 1)
      return
  histogram.append((word, 1))
    

## histogram list of lists implementation
# def histogram(file):
#   '''
#   Takes file as argument, reads file and counts word frequency stores freq in dict. returns a dictionary
#   '''
#   histogram = []
#   text = open(file, 'r').read()
#   words = [word for line in text.split('\n') for word in line.split(' ')]
#   for word in words:
#     add_word_to_histogram(histogram, word)
#   return histogram

# def add_word_to_histogram(histogram, word):
#   '''
#   Adds a word or freq to list in histogram list
#   '''
#   for arr in histogram:
#     if arr[0] == word:
#       arr[1] += 1
#       return
#   histogram.append([word, 1])

## histogram dictionary implementation
# def histogram(file):
#   '''
#   Takes file as argument, reads file and counts word frequency stores freq in dict. returns a dictionary
#   '''
#   # pattern = re.compile(r"[^a-zA-Z0-9]") trying to implement this to clean string from file
#   word_freq = {}
#   word_file = open(file, 'r').read()
#   word_arr = word_file.split(' ')
#   for word in word_arr:
#     if word in word_freq:
#       word_freq[word] += 1
#     else:
#       word_freq[word] = 1
#   return word_freq

def unique_words(hist):
  '''
  Given a histogram returns total count of unique words (returns Int)
  '''
  return len(hist)

def frequency(word, hist):
  '''
  Given a word as input returns frequency of word (reads from histogram)
  '''
  if word in hist:
    return hist[word]
  else: 
    return "The word inputted was not in histogram."


def generate_sentence(hist, length):
  '''
  Given a histogram and length of sentence, generates a random sentence with "randomness" weighted towards frequency
  '''
  word_arr = []
  rand_sentence = []
  for key in hist:
    for _ in range(hist[key]):
      word_arr.append(key)
  

  

  



if __name__ == '__main__':
  my_dict = histogram(input('Please input a file name: '))
  print(my_dict)
  # print(unique_words(my_dict))
  # print(frequency('word', my_dict))
  # print('gen sentence****', generate_sentence(my_dict, 5))
