from flask import Flask, jsonify, render_template
import histogram as h

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/tweets')
def tweets():
  my_dict = h.histogram('histo_text.txt')
  tweet = h.generate_sentence(my_dict, 15)
  return jsonify({ 'tweet': tweet })
