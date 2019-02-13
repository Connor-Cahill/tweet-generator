from dictogram import Dictogram
import string

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
    """compiles a first order markov chain """
    words = [word for line in text.split('\n') for word in line.split(' ')] # Split sentence into list of words 
    for i in range(len(words) - 1): ## -1 to account for word after 
      if words[i] not in self:
        self[words[i]] = Dictogram()
      self[words[i]].add_count(words[i + 1])
    

  
  def pick_word_from(self, dictogram):
    """Given a dictogram returns a probable word """
    pass
  

def main():
  """ Calls some markov chain methods """
  with open('histo_text.txt') as file:
    text = file.read()
    new_text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    new_text = new_text.translate(translator)
  m_chain = Markov_Chain(new_text)
  print(m_chain)


if __name__ == "__main__":
  main()

