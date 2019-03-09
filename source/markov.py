import nltk
import random 
import json
import pandas as pd
import numpy
import pickle
import re
from source.dictogram import Dictogram

class Markov_Chain(Dictogram):
  """ Markov Chain class """
  def __init__(self, text=None, dictogram=None):
    """Initiates new instance of Markov Chain class """
    super(Markov_Chain, self).__init__() # creates new instance of Markov Chain
    self.sentence_starters = [] # list of words that start sentences
    if text is not None:
      sentences = nltk.sent_tokenize(text)  #  nltk.sent_tokenize returns an array of text split by sentences
      for sent in sentences:
          if len(sent) > 4:
            self.create_two(sent) # pass each sentence through the create method
    if dictogram is not None:
        self = dictogram



  def create(self, words):
    """Creates a first order markov chain """
    words = words.split(' ')
    if words[0] not in self:  # checks to see if starting word in dict 
      self[words[0]] = Dictogram() # creates list to keep track of start value
      self.sentence_starters.append(words[0]) # add word to sentence starters list
    self[words[0]].add_count(words[1])  # if already in self, adds to count 
    last_index = len(words) -1 #  grab last index in words list
    if words[last_index] not in self:
      self[words[last_index]] = "###" # add the end token
    for i in range(len(words) - 1): # -1 to account for word after 
      if words[i] not in self:  # if word not in self
        self[words[i]] = Dictogram()  # add empty dictogram for word
    if not isinstance(self[words[i]], str):
        self[words[i]].add_count(words[i + 1])  # call dictograms add_count method with the words that follows
  
  def create_two(self, sentence):
    """creates and compiles 2nd order markov chain"""
    # make arr of words from sentence 
    words = sentence.split(' ') 

    # check that their are enough words
    if len(words) > 2:
      # add first 2 words to sentence starters
      self.sentence_starters.append((words[0], words[1]))
      last_index = len(words) - 1 #  grab last index in words list
      # get last word pair in sentence (last 2 words)
      last_pair = (words[last_index - 1], words[last_index])
      if last_pair not in self:
        self[last_pair] = "###" # add the end token
      # loop through word list
      for i in range(len(words) - 2):
        # get current and next word 
        word_pair = (words[i], words[i + 1])
        # check if word pair is new
        if word_pair not in self:
          # create a new dictogram 
          self[word_pair] = Dictogram()
        # run add count method with 3rd word out
        if not isinstance(self[word_pair], str):
            self[word_pair].add_count(words[i + 2])

  def create_two_str(self, sent):
    """Creates a 2nd order markov chain using strings instead of tuples """
    words = sent.split(' ')
    window = ''
    if len(words) > 2:
        # load first 2 words in window
        window += '{} {}'.format(words[0], words[1])
        # add words to sentence starters
        self.sentence_starters.append(window)
        # reset window
        window = ''
        # get last index
        last_indx = len(words) - 1
        # load last pair into window
        window += words[last_indx - 1] + words[last_indx]
        # is the pair already in self?
        if window not in self:
            # add the stop token indicator
            self[window] = '###'
        # loop through word list
        for i in range(len(words) - 2):
            # reset the window
            window = ''
            # add new values to window
            window += '{} {}'.format(words[i], words[i + 1])
            if window not in self:
                self[window] = Dictogram()
            if not isinstance(self[window], str):
                # add count of 2nd word out
                self[window].add_count(words[i + 2])

  
  #* Test this method
  def create_n(self, sentence, n):
    """ creates a nth order markov chain """
    words = sentence.split(' ') 
    ends = '!?.'
    # make sure there is enough words
    if len(words) > n:
      # loop over length of words - order
      for i in range(len(words) - n):
        # creates tuple of 'n' words 
        word_tup = tuple(word for word in words[i:i+n])
        # check if enough words in tuple
        if len([i for i in word_tup if i[-1] not in ends]) == n:
          if word_tup not in self:
            # if tup not in self, create new dict
            self[word_tup] = Dictogram()
          # adds nth word out
          self[word_tup].add_count(words[i + n])  # dictograms add_count method

  def pick_word_from(self, dictogram):
    """Given a dictogram returns a probable word """
    accumulator = 0
    seperators = []
    words = [word for word in dictogram.keys()]
    # Create a list of ints that act as seperator for weights
    for _, weight in dictogram.items():
      accumulator += weight
      seperators.append(accumulator)
      rand_num = random.randint(0, accumulator)
      ## Iterate through separators and find selected word with random num
    for i, s in enumerate(seperators):
      if rand_num <= s:
        return words[i] 

  #! currently only words for first order markov chain
  def generate_sentence(self):
    """Generates a sentence with pick_word_from and random walk through markov chain """
    words = [word for word in self.keys()]  # create list of words in markov_chain
    sentence = '' # create empty sentence
    word = random.choice(self.sentence_starters)  # grab random starting word
    sentence += word
    while self[word] != "###":  # while word isn't end token
      word = self.pick_word_from(self[word])  # pick random word
      sentence += ' ' + word  # append word to sentence
    return sentence  
  
  def gen_sentence_2nd_order(self):
    """ generates a random sentence from 2nd order markov chain """
    sentence_list = []
    # get random sentence starter word pair
    word_pair = random.choice(self.sentence_starters)
    sentence_list.append(word_pair[0]) 
    sentence_list.append(word_pair[1])
    # iterate until end token is hit
    while self[word_pair] != "###":
      word = self.pick_word_from(self[word_pair])  # grab random word
      sentence_list.append(word)  #  append word to sentence 
      word_pair = (sentence_list[-2], sentence_list[-1])

    return ' '.join(sentence_list)

    def gen_sentence_2nd_order_str(self):
        """Generates a sentence for higher order markov chain string implementation"""
        sentence_list = []
        # get random sentence starter
        word_pair = random.choice(self.sentence_starters)
        word_pair = word_pair.split(' ')
        sentence_list.append(word_pair[0])
        sentence_list.append(word_pair[1])
        # iterate until stop token
        while self[word_pair] != '###':
            word = self.pick_word_from(self[word_pair])
            sentence_list.append(word)
            word_pair = '{} {}'.format(sentence_list[-2], sentence_list[-1])
        return ' '.join(sentence_list)



  def serialize_markov(self, file):
      """Serializes a large markov chain to a file that can later be retrieved"""
      with open(file) as cur_file:
        pickle.dump(self, cur_file)


  def deserialize_markov(self, file):
      """Retrieves and deserializes markov chain from inputted file"""
      with open(file) as cur_file:
        return pickle.load(cur_file)

#*  sample sentences with start and stop tokens
# They think beyond the only option, but often there are trade-offs involved.
# What distinguishes Pragmatic Programmers? - 2nd order
# We feel it’s an attitude, a style, a philosophy of approaching problems and their solutions. - 2nd order

def main():
  """ Calls some markov chain methods """
  with open('histo_text.txt') as file:
    text = file.read()
    # new_text = text.lower()
    # new_text = new_text.translate(translator)
  m_chain = Markov_Chain(text)
  # print(m_chain)
  # print(m_chain.pick_word_from(m_chain['fish']))
  # for _, v in enumerate(m_chain.keys()):
  #   m_chain.pick_word_from(m_chain[v])
  print(m_chain.gen_sentence_2nd_order())


def test_the_markov():
    """Runs test on markov"""
    df_csv = pd.read_csv('employee_reviews.csv', usecols=[6, 7, 8])
    df = json.loads(df_csv.to_json())
    pros_list = [item for item in df['pros'].values()]
    cons_list = [item for item in df['cons'].values()]

    output_list = []
    for i in range(len(pros_list)):
        pro = pros_list[i]
        con = cons_list[i]
        if len(pro) > 8:
            output_list.append(pro)
        else:
            print('pro too small')
        if len(con) > 8:
            output_list.append(con)
        else:
            print('con too small')
    m_chain = Markov_Chain(output_list)
    print(m_chain.generate_sentence())


def small_test_markov():
    with open('histo_text.txt') as file:
        text = file.read()
    m_chain = Markov_Chain(text)
    print(m_chain.gen_sentence_2nd_order())


if __name__ == "__main__":
    small_test_markov()
