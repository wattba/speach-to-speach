from flask import Flask, render_template, request
import sys
from aws_translation import translate
from flask import jsonify

app = Flask(__name__)
@app.route('/get_task', methods=['GET'])
def get_tasks():
  input_txt = 'Hello' # request.form['input_txt']
  src_lang = 'en' #request.form['src_lang']
  dst_lang = 'de' #request.form['dst_lang']
  
  output_txt = translate(input_txt, src_lang, dst_lang)
  return jsonify({'translation':output_txt})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
