from flask import Flask,request,jsonify
from openai import OpenAI 
import apienv.constants
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)
client = OpenAI(
    
    api_key=(apienv.constants.api_key),
)

def CustomChatGPTbooks(topic,type):
    Book_response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
    {"role": "system", "content": f"just give a list of the best{type} to learn about the given subject"},
    {"role": "user", "content": topic}
  ]
    )

    ChatGPT_reply = [Book_response.choices[0].message.content]
    split_response = ChatGPT_reply[0].split('\n')
    split_response_just_numberlist = []
    for responses in split_response:
        if responses[0].isnumeric():
            split_response_just_numberlist.append(responses)

    return split_response_just_numberlist


@app.route('/post', methods=["POST"])
def send():
     input_json = request.get_json(force=True) 
     topic = input_json['topic']
     type_of = input_json['type']
     response = CustomChatGPTbooks(topic,type_of)
     return jsonify(response)

if __name__== '__main__':
    app.run(debug=True)
