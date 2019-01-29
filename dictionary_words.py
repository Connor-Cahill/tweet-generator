import random

def words_from_dict(num_words):
  '''
Takes num words as argument and returns n random words from dictionary
  '''
  rand_word_arr = []
  word_file = open('/usr/share/dict/web2', 'r').read().splitlines()
  for i in range(num_words):
    rand_word = random.choice(word_file)
    rand_word_arr.append(rand_word)
  return ' '.join(rand_word_arr)

if __name__ == '__main__':
  num_words = int(input('How many words in the sentence? '))
  print(words_from_dict(num_words))
