from flask import Flask
import histogram as h

app = Flask(__name__)

@app.route('/')
def triggerSentence():
  my_dict = h.histogram('histo_text.txt')
  sentence = h.generate_sentence(my_dict, 15)
  return str(sentence)
