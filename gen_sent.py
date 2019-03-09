import random

class Tweet_Generator:
    """generates tweets using a pickled markov chain file and sentence starters"""
    def __init__(self, markov, starters):
        """Creates new instance of tweet generator class"""
        self.markov = markov
        self.starters = starters # sentence starters

    def pick_word_from(self):
        """Picks a random word from a markov chain"""
        accumulator = 0
        seperators = []
        words = self.markov.keys()
 
        for word, weight in self.markov.items():
            accumulator += weight
            seperators.append(accumulator)
 
        rand_num = random.randint(0, accumulator)
        for i, s in enumerate(seperators):
            if rand_num <= s:
                return words[i]

    def generate_sentence(self):
        """Generates a sentence given a 2nd order markov chain"""
        sentence_list = []  # create empty arr for sent
        # get random starting word
        word_pair = random.choice(self.starters)
        sentence_list.append(word_pair[0])
        sentence_list.append(word_pair[1])
        # iterate until stop token
        while self.markov[word_pair] != '###':
            word = self.pick_word_from()
            sentence_list.append(word)
            word_pair = (sentence_list[-2], sentence_list[-1])
        # return the joined list of words
        return ' '.join(sentence_list)

