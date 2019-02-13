from dictogram import Dictogram

class Markov_Chain(Dictogram):
  """ Markov Chain class """
  def __init__(self, sentences):
    """Initiates new instance of Markov Chain class """
    super(Markov_Chain, self).__init__() # creates new instance of Markov Chain
    self.sentence_starters = Dictogram()
    for sent in sentences:
      pass #! Finish creation of Markov Chain

  #First order Markov chain compile
  def compile(self, sentence):
    """compiles a first order markov chain """
    words = sentence.split(' ') # Split sentence into list of words 
    ## iterate over words
    for i, w in enumerate(words):
      if w not in self:
        self[w] = Dictogram()
      self[w].add_count(words[i + 1])
  

  # Second order Markov Chain
  def compile2(self):
    pass 
  
  def pick_word_from(self, dictogram):
    """Given a dictogram returns a probable word """
    pass
        

