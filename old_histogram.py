import re, random, string, sys
'''
NOTE:
This file is old and refactored into the histograms file as classes 
'''

#histogram list of tuples implementation
def tupleagram(file):
  '''
  Takes file as argument, reads file and counts word frequency stores freq in dict. returns a dictionary
  '''
  histogram = []
  with open(file, 'r') as word_file:
    # calls fix text function(cleans up the string)
    text = fix_text(word_file.read())
    # creates an array of words
    words = [word for line in text.split('\n') for word in line.split(' ')]
  for word in words:
    # for every word in arr, call helper tupleagram function
    add_word_to_tupleagram(histogram, word)
  return sort_histogram(histogram)


def add_word_to_tupleagram(histogram, word):
  '''
  Adds a word or freq to tuple in histogram list
  '''
  for i in range(len(histogram)):
    if histogram[i][0] == word:
      # if word already in tupleagram, update tuple
      histogram[i] = (word, histogram[i][1] + 1)
      return
  histogram.append((word, 1))
    

## Implementation of a "countagram" 
def countagram(file):
  '''
  Takes file as argument and returns a histogram as odd data structure
  '''
  histogram = [(1, [])]
  ## Opens file and creates Arr (words) of words 
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
      # if word is in hist already, remove from that freq list and move to next
      histogram[i][1].remove(word)
      # check if proper frequency index already exists 
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
  # create arr of words from file
  with open(file, 'r') as word_file:
    text_file = word_file.read().lower()
    text = fix_text(text_file)
    words = [word for line in text.split('\n') for word in line.split(' ')]
  for word in words:
    add_word_to_listogram(histogram, word)
  return sort_histogram(histogram)

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
    # cleans up string 
    text = fix_text(file_string)
    # creates list of words from file (splits at newline and then spaces)
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
  
############  
### Random sentence generator and word pick with freq weights
###############
def generate_sentence(histogram, length):
  '''
  Given a histogram, creates a random sentence with "randomness" weighted towards freq
  '''
  random_sentence = []
  for i in range(length):
    word = pick_word(histogram)
    random_sentence.append(word)
  return ' '.join(random_sentence)

def pick_word(histogram):
  '''
  Given a histogram function will pick a random word based on the frequency weights
  '''
  accumulator = 0
  separators = []
  words = [word for word in histogram.keys()]
  # creates a list of ints that act as separators for weights
  for _, weight in histogram.items():
    accumulator += weight
    separators.append(accumulator)
  rand = random.randint(0, accumulator)
  ## returns the word at index of the weight in 
  #seperators list that is greater than rand
  for i, s in enumerate(separators):
    if rand <= s:
      return words[i]


### Generate sentence listogram implementation
def random_sentence_lol(listogram, length):
  '''
  Takes in a listogram and creates a random sentences base on freq weights
  '''
  rand_sentence = []
  for i in range(length):
    word = pick_word_listogram(listogram)
    rand_sentence.append(word)
  return ' '.join(rand_sentence)

## for list of lists histogram (same as other pick_word function just for list of lists)
def pick_word_listogram(listogram):
  '''
  Takes a listogram and picks a word using frequency as weight
  '''
  accumulator = 0
  seperators = []
  # creates list from words in listogram
  words = [lst[0] for lst in listogram]
  # creates list of weights in listogram 
  weights = [lst[1] for lst in listogram]

  # add weight to accumulator and append value to separator arr
  for weight in weights:
    accumulator += weight
    seperators.append(accumulator)

  rand = random.randint(0, accumulator)
  for i, s in enumerate(seperators):
    # if the random number is smaller than separator value return the word
    if rand <= s:
      return words[i]

## sorts list of list histogram
def sort_histogram(histogram):
  '''
  Sorts list histogram by its values (frequency)
  '''  
  for i in range(len(histogram)):
    for j in range(len(histogram)):
      # checking the freq value in listogram (comparing)
      if histogram[j][1] > histogram[i][1]:
        histogram[j], histogram[i] = histogram[i], histogram[j]
  return histogram
  
def test_pick_word(histo):
  '''
  Tests the pick_word function to see if weighting is accurate
  '''
  test = {}
  for i in range(10000):
    word = pick_word(histo)
    if word in test:
      test[word] += 1
    else:
      test[word] = 1
  histo_to_file('test_histo.txt', test)
  return test
      

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
  my_dict = histogram(file)
  # print(my_dict)
  test_pick_word(my_dict)
  # print(generate_sentence(my_dict, 10))

