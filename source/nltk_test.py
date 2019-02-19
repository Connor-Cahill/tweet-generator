import nltk
if __name__ == "__main__":
  with open('histo_text.txt') as file:
    text = file.read()
  sents = nltk.sent_tokenize(text)
  print(sents)

  

  