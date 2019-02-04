import random, itertools



def reverse_word(word):
  '''
  Takes in a word/sentence and reverses it
  '''
  new_word = ''
  i = 0
  while abs(i) < len(word):
    i -= 1
    new_word += word[i]
  return new_word


def auto_complete(string_base):
  '''
  Takes in a string base and suggests words to you 
  '''
  suggestions = []
  with open('/usr/share/dict/web2') as word_file:
    text = word_file.read()
    words = [word for word in text.split('\n')]
  for word in words:
    if string_base in word:
      suggestions.append(word)
  return 'Suggested Words:\n{}'.format('\n-'.join(suggestions))
    

def words_from_dict(num_words):
  '''
Takes num words as argument and returns n random words from dictionary
  '''
  rand_word_arr = []
  # word_file = open('/usr/share/dict/web2', 'r').read().splitlines()
  with open('/usr/share/dict/web2', 'r') as word_file:
    words = word_file.readlines() # why does this not return string on same line???
    # words = word_file.read().splitlines()
    

  for i in range(num_words):
    rand_word = random.choice(words)
    rand_word_arr.append(rand_word)
  return ' '.join(rand_word_arr)


def anagram_generator(string):
  '''
  Takes in a string and returns array of anagrams of string
  '''
  ret = [''.join(perm) for perm in itertools.permutations(string)]
  return ret

if __name__ == '__main__':
  # num_words = int(input('How many words in the sentence? '))
  # print(words_from_dict(num_words))
  # print(reverse_word('hello'))
  # print(anagram_generator('hello'))
  print(auto_complete('hell'))



