import re, random

#histogram list of tuples implementation
def tupleagram(file):
  '''
  Takes file as argument, reads file and counts word frequency stores freq in dict. returns a dictionary
  '''
  histogram = []
  text = open(file, 'r').read()
  words = [word for line in text.split('\n') for word in line.split(' ')]
  for word in words:
    add_word_to_tupleagram(histogram, word)
  return histogram


def add_word_to_tupleagram(histogram, word):
  '''
  Adds a word or freq to tuple in histogram list
  '''
  for i in range(len(histogram)):
    if histogram[i][0] == word:
      histogram[i] = (word, histogram[i][1] + 1)
      return
  histogram.append((word, 1))
    

# histogram list of lists implementation
def listogram(file):
  '''
  Takes file as argument, reads file and counts word frequency stores freq in dict. returns a dictionary
  '''
  histogram = []
  text = open(file, 'r').read()
  words = [word for line in text.split('\n') for word in line.split(' ')]
  for word in words:
    add_word_to_listogram(histogram, word)
  return histogram

def add_word_to_listogram(histogram, word):
  '''
  Adds a word or freq to list in histogram list
  '''
  for arr in histogram:
    if arr[0] == word:
      arr[1] += 1
      return
  histogram.append([word, 1])

# histogram dictionary implementation
def histogram(file):
  '''
  Takes file as argument, reads file and counts word frequency stores freq in dict. returns a dictionary
  '''
  histogram = {}
  text = open(file, 'r').read()
  words = [word for line in text.split('\n') for word in line.split(' ')]
  for word in words:
    if word in histogram:
      histogram[word] += 1
    else:
      histogram[word] = 1
  
  histo_to_file('histo_results.txt', histogram)
  return histogram

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

def histo_to_file(file, histogram):
  '''
  Takes a histogram and writes it to a file
  '''
  with open(file, 'w+') as text_file:
    text_file.write('\n****** NEW HISTOGRAM RESULTS *******\n')
    for key, value in histogram.items():
      text_file.write('{} : {}\n'.format(key, value))
  
  

def generate_sentence(file, length):
  '''
  Given a file and length of sentence, generates a random sentence with "randomness" weighted towards frequency
  '''
  random_sentence = []
  text = open(file, 'r').read()
  words = [word for line in text.split('\n') for word in line.split(' ')]
  for _ in range(length):
    word = random.choice(words)
    random_sentence.append(word)
  return ' '.join(random_sentence)
  

  

  



if __name__ == '__main__':
  my_dict = histogram(input('Please input a file name: '))
  print(my_dict)
  # print(listogram(input('Please input a file name: (listogram implementation)')))
  # print(tupleagram(input('Please input a file name: (tupleagram implementation)')))
  # print(unique_words(my_dict))
  # print(frequency('word', my_dict))
  # print(generate_sentence(input('Please input a text file: '), 5))

