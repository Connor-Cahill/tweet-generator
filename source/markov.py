from dictogram import Dictogram
import nltk
import string, random

class Markov_Chain(Dictogram):
  """ Markov Chain class """
  def __init__(self, text=None):
    """Initiates new instance of Markov Chain class """
    super(Markov_Chain, self).__init__() # creates new instance of Markov Chain
    self.sentence_starters = [] # list of words that start sentences
    if text is not None:
      sentences = nltk.sent_tokenize(text)  #*  nltk.sent_tokenize returns an array of text split by sentences
      for sent in sentences:
        sent = sent.replace('\n', ' ')  # replace newline chars in each sentence
        self.create(sent) # pass each sentence through the create method
      

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

  def generate_sentence(self):
    """Generates a sentence with pick_word_from and random walk through markov chain """
    words = [word for word in self.keys()]  # create list of words in markov_chain
    sentence = '' # create empty sentence
    word = random.choice(self.sentence_starters)  # grab random starting word
    while self[word] != "###":  # while word isn't end token
      word = self.pick_word_from(self[word])  # pick random word
      sentence += ' ' + word  # append word to sentence
      ret = sentence.capitalize() # capitalize first letter in sentence
    return ret  


def main():
  """ Calls some markov chain methods """
  with open('histo_text.txt') as file:
    text = file.read()
    # new_text = text.lower()
    # new_text = new_text.translate(translator)
  m_chain = Markov_Chain(text)
  print(m_chain)
  # print('STARTERS: ', m_chain.sentence_starters)
  # print('ENDERS: ', m_chain.sentence_enders)
  # print(m_chain.pick_word_from(m_chain['fish']))
  # for _, v in enumerate(m_chain.keys()):
  #   m_chain.pick_word_from(m_chain[v])
  # print(m_chain.generate_sentence())


if __name__ == "__main__":
  main()
  
