from flask import Flask, jsonify, render_template
from source.markov import Markov_Chain
import pickle

app = Flask(__name__)


def serialize_markov(markov_chain, file):
  """Serializes a large markov chain to a file that can later be retrieved"""
  with open(file) as cur_file:
    pickle.dumps(markov_chain, cur_file)


def deserialize_markov(file):
  """Retrieves and deserializes markov chain from inputted file"""
  with open(file) as cur_file:
    return pickle.load(cur_file)

def generate_markov():
    """generates and saves markov chain"""
    with open('big-text.txt') as big_text:
        text = big_text.read()
    text = text.replace('\n', ' ')
    mark = Markov_Chain(text)
    serialize_markov(mark, 'markov.pickle')

@app.route('/')
def index():
    """Renders the main.html template at GET: '/' """
    return render_template('main.html')


@app.route('/tweets')
def tweets():
    """Sends a json object containing a randomly generated tweet """
    with open('review_text_file.txt') as file:
        text = file.read()
    markov_chain = Markov_Chain(text)
    tweet = markov_chain.gen_sentence_2nd_order()
    return jsonify({'tweet': tweet})

if __name__ == '__main__':
   generate_markov() 
