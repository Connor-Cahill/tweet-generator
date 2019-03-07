from flask import Flask, jsonify, render_template
from source.markov import Markov_Chain

app = Flask(__name__)


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
