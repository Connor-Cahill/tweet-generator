import nltk
import string, random
from source.dictogram import Dictogram

class Markov_Chain(Dictogram):
  """ Markov Chain class """
  def __init__(self, text=None):
    """Initiates new instance of Markov Chain class """
    super(Markov_Chain, self).__init__() # creates new instance of Markov Chain
    self.sentence_starters = [] # list of words that start sentences
    if text is not None:
        self.create_two(text)
      # sentences = nltk.sent_tokenize(text)  #*  nltk.sent_tokenize returns an array of text split by sentences
      # for sent in sentences:
        # self.create_two(sent) # pass each sentence through the create method
      

  def create(self, sentence):
    """creates a first order markov chain """
    words = sentence.split(' ') # creates list of words in inputted sentence
    if words[0] not in self:  # checks to see if starting word in dict 
      self[words[0]] = Dictogram() # creates list to keep track of start value
      self.sentence_starters.append(words[0]) # add word to sentence starters list
    self[words[0]].add_count(words[1])  # if already in self, adds to count 
    last_index = len(words) -1 #  grab last index in words list
    if words[last_index] not in self:
      self[words[last_index]] = "###" # add the end token
    for i in range(len(words) - 1): ## -1 to account for word after 
      if words[i] not in self:  # if word not in self
        self[words[i]] = Dictogram()  # add empty dictogram for word
      self[words[i]].add_count(words[i + 1])  # call dictograms add_count method with the words that follows
  
  def create_two(self, sentence):
    """creates and compiles 2nd order markov chain"""
    # make arr of words from sentence 
    words = sentence.split(' ') 

    # check that their are enough words
    if len(words) > 2:
      # add first 2 words to sentence starters
      self.sentence_starters.append((words[0], words[1]))
      last_index = len(words) -1 #  grab last index in words list
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
        self[word_pair].add_count(words[i + 2])
  
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


if __name__ == "__main__":
  main()
  
