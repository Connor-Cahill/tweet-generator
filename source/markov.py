from dictogram import Dictogram
import nltk
import string, random

class Markov_Chain(Dictogram):
  """ Markov Chain class """
  def __init__(self, text=None):
    """Initiates new instance of Markov Chain class """
    super(Markov_Chain, self).__init__() # creates new instance of Markov Chain
    self.sentence_starters = Dictogram()
    self.sentence_enders = Dictogram()
    if text is not None:
      sentences = nltk.sent_tokenize(text)
      for sent in sentences:
        sent = sent.replace('\n', ' ')
        self.create(sent)
      

  #First order Markov chain compile
  def create(self, sentence):
    """creates a first order markov chain """
    # words = [word for line in text.split('\n') for word in line.split(' ')] # Split sentence into list of words 
    words = sentence.split(' ')
    self.sentence_starters.add_count(words[0])  # runs add_count method on sentence starters dictogram
    self.sentence_enders.add_count(words[-1]) # same as above but for sentence enders 
    for i in range(1, len(words) - 2): ## -1 to account for word after 
      if words[i] not in self:
        self[words[i]] = Dictogram()
      self[words[i]].add_count(words[i + 1])
  

  
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

  def generate_sentence(self, length):
    """Generates a sentence with pick_word_from and random walk through markov chain """
    words = [word for word in self.keys()]
    sentence = ''
    word = random.choice(words) ## randomly picks first word unweighted
    for i in range(length):
      word = self.pick_word_from(self[word])
      sentence += ' ' + word
    return sentence


def main():
  """ Calls some markov chain methods """
  with open('histo_text.txt') as file:
    text = file.read()
    # new_text = text.lower()
    # new_text = new_text.translate(translator)
  m_chain = Markov_Chain(text)
  # print(m_chain)
  print('STARTERS: ', m_chain.sentence_starters)
  print('ENDERS: ', m_chain.sentence_enders)
  # print(m_chain.pick_word_from(m_chain['fish']))
  # for _, v in enumerate(m_chain.keys()):
  #   m_chain.pick_word_from(m_chain[v])
  # print(m_chain.generate_sentence(20))


if __name__ == "__main__":
  main()
  
