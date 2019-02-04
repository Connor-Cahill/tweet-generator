import re, random, string, sys

#histogram list of tuples implementation
def tupleagram(file):
  '''
  Takes file as argument, reads file and counts word frequency stores freq in dict. returns a dictionary
  '''
  histogram = []
  with open(file, 'r') as word_file:
    text = word_file.read()
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
    

## Implementation of a "countagram" 
def countagram(file):
  '''
  Takes file as argument and returns a histogram as odd data structure
  '''
  histogram = [(1, [])]
  with open(file) as word_file:
    file_string = word_file.read().lower()
    text = fix_text(file_string)

    words = [word for line in text.split('\n') for word in line.split(' ')]
  for word in words:
    add_to_countagram(histogram, word)
  
  return histogram

def add_to_countagram(histogram, word):
  '''
   Adds a word or freq to tuple in histogram list
  '''
  for i in range(len(histogram)):
    if word in histogram[i][1]:
      histogram[i][1].remove(word)
      if len(histogram) > i + 1:
        histogram[i + 1][1].append(word)
        return
      else:
        histogram.append((i + 1, []))
        histogram[i + 1][1].append(word)
        return
  histogram[0][1].append(word)
    
# histogram list of lists implementation
def listogram(file):
  '''
  Takes file as argument, reads file and counts word frequency stores freq in dict. returns a dictionary
  '''
  histogram = []
  with open(file, 'r') as word_file:
    text = word_file.read().lower()
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
  with open(file, 'r') as word_file:
    file_string = word_file.read()
    text = fix_text(file_string)
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
  
  

def generate_sentence(histogram, length):
  '''
  Given a histogram, creates a random sentence with "randomness" weighted towards freq
  '''
  unique = unique_words(histogram)
  words = [k for k, v in histogram.items()]
  weights_dict = {}
  for word in words:
    weight = histogram[word] / unique
    weights_dict[word] = weight
  return weights_dict
  
## sorts list of list histogram
def sort_histogram(histogram):
  '''
  Sorts list histogram by its values (frequency)
  '''  
  for i in range(len(histogram)):
    for j in range(len(histogram)):
      if histogram[j][1] > histogram[i][1]:
        histogram[j], histogram[i] = histogram[i], histogram[j]
  return histogram
  


def fix_text(text):
  '''
  takes in takes and strips puncaution and make all words lowercase
  '''
  new_text = text.lower()
  translator = str.maketrans('', '', string.punctuation)
  ret = new_text.translate(translator)
  return ret

  

if __name__ == '__main__':
  file = sys.argv[1]
  # num_words = sys.argv[2] //  this will be for when I use random_sentence_gen
  # my_dict = histogram(file)
  my_dict = listogram(file)
  # print(my_dict)
  print(sort_histogram(my_dict))
  # my_dict = countagram(file)
  # print(my_dict)
  # print(listogram(file)
  # print(tupleagram(file)
  # print(unique_words(my_dict))
  # print(frequency('word', my_dict))
  # print(generate_sentence(my_dict, 5))

