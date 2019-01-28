import random

def rearrange_string(sentence):
  '''
  Takes in sentence as user input and returns a random sentence with the same words
  '''
  str_arr = sentence.split(' ')
  random_order = []
  for i in range(len(str_arr)):
    rand_word = random.choice(str_arr)
    str_arr.pop(str_arr.index(rand_word))
    random_order.append(rand_word)
  new_string = ' '.join(random_order)
  return new_string
  

    



if __name__ == '__main__':
  print(rearrange_string('how now brown cow'))