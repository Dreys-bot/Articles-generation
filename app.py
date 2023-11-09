from flask import Flask, render_template, request, jsonify
from tunetesting import generate_n_text_samples
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import os

app = Flask(__name__,
            static_url_path='', 
            static_folder='templates',)

@app.route('/')
def index():
    return render_template('index.html')

model_headlines_path = './new-articles_v4'


headlines_model = GPT2LMHeadModel.from_pretrained(model_headlines_path)
headlines_tokenizer = GPT2Tokenizer.from_pretrained(model_headlines_path)

device = "cpu"


@app.route('/get_response')
def get_response():
    print("user")
    user_query = request.args.get('msg')
    print("user_query", user_query)
    response = generate_n_text_samples(headlines_model, headlines_tokenizer, 
                                    user_query, device, n_samples = 2)
    response_string = str(response[0])
    print("response", response_string)

    return jsonify({'response': response_string})


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0')