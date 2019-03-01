import random

def rearrange_string(sentence):
  '''
Takes in sentence as user input and returns a random sentence with the same words
  '''
  str_arr = sentence.split(' ')
  for i in range(len(str_arr)):
    rand_int = random.randint(0, len(str_arr) - 1)
    str_arr[rand_int], str_arr[i] = str_arr[i], str_arr[rand_int]
  return ' '.join(str_arr)


if __name__ == '__main__':
  print(rearrange_string('how now brown cow'))
