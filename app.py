from flask import Flask, jsonify, render_template
from source.markov import Markov_Chain

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')



@app.route('/tweets')
def tweets():
  with open('histo_text.txt') as file:
    text = file.read()
  markov_chain = Markov_Chain(text)
  tweet = markov_chain.gen_sentence_2nd_order()
  return jsonify({ 'tweet': tweet })
