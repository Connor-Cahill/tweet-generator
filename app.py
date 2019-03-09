from flask import Flask, jsonify, render_template
from source.markov import Markov_Chain
from markov import markov, sentence_starters
from gen_sent import Tweet_Generator 
import pickle
import json

app = Flask(__name__)


def serialize_markov(markov_chain, file):
  """Serializes a large markov chain to a file that can later be retrieved"""
  with open(file, "wb") as cur_file:
    pickle.dump(markov_chain, cur_file)

def serialize_sent_starters(sent_starts, file):
    """Serializes the markov_chain sentence starters"""
    with open(file, "wb") as sent_file:
        pickle.dump(sent_starts, sent_file)


def deserialize_markov(file, sent_start_file):
  """Retrieves and deserializes markov chain from inputted file"""
  with open(file, "rb") as cur_file:
    return pickle.load(cur_file)

def generate_markov():
    """generates and saves markov chain"""
    with open('big-text.txt') as big_text:
        text = big_text.read()
    text = text.replace('\n', ' ')
    mark = Markov_Chain(text)
    print('Serializing Markov Chain ... ')
    serialize_markov(mark, 'markov.pickle')
    serialize_sent_starters(mark.sentence_starters, 'sent_starters.pickle')


@app.route('/')
def index():
    """Renders the main.html template at GET: '/' """
    return render_template('main.html')


@app.route('/tweets')
def tweets():
    """Sends a json object containing a randomly generated tweet """
    #m_chain = Markov_Chain(None, markov) 
    #tg = Tweet_Generator(m_chain, sentence_starters)
    #tweet = tg.generate_sentence()
    with open('big-text.txt') as file:
        big_text = file.read()
    m_chain = Markov_Chain(big_text)
    tweet = m_chain.gen_sentence_2nd_order()
    return jsonify({'tweet': tweet})


def small_markov_test():
    """tests markov chain with smaller block of text and gens sentence
    shows the 2nd order markov chain is working and can generate sentences"""
    with open('histo_text.txt') as file:
        text = file.read()
    mm = Markov_Chain(text)
    print(mm.gen_sentence_2nd_order())

if __name__ == '__main__':
    small_markov_test() 
