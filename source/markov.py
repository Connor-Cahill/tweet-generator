from dictogram import Dictogram
import string, random

class Markov_Chain(Dictogram):
  """ Markov Chain class """
  def __init__(self, text=None):
    """Initiates new instance of Markov Chain class """
    super(Markov_Chain, self).__init__() # creates new instance of Markov Chain
    self.sentence_starters = Dictogram()
    if text is not None:
      self.create(text)
      

  #First order Markov chain compile
  def create(self, text):
    """creates a first order markov chain """
    words = [word for line in text.split('\n') for word in line.split(' ')] # Split sentence into list of words 
    for i in range(len(words) - 1): ## -1 to account for word after 
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
    new_text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    new_text = new_text.translate(translator)
  m_chain = Markov_Chain(new_text)
  # print(m_chain.pick_word_from(m_chain['fish']))
  # for _, v in enumerate(m_chain.keys()):
  #   m_chain.pick_word_from(m_chain[v])
  print(m_chain.generate_sentence(7))


if __name__ == "__main__":
  main()
  
