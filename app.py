from flask import Flask,request,jsonify
from openai import OpenAI 
# import apienv.constants
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

client = OpenAI(
    
    api_key=('j'),
)

def find_results(topic,type):
    raw_response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
    {"role": "system", "content": f"just give a list of the best{type} to learn about the given subject"},
    {"role": "user", "content": topic}
  ]
    )

    openai_reply = [raw_response.choices[0].message.content]
    split_response = openai_reply[0].split('\n')
    send = []
    for response in split_response:
        if len(response) != 0 and response[0].isnumeric():
            send.append(response)
    if send == []:
        send = [f'Sorry we could not find any {type} on {topic}']

        
            

            

    return send


@app.route('/post', methods=["POST"])
@cross_origin()
def send():
     input_json = request.get_json(force=True) 
     topic = input_json['topic']
     type_of = input_json['type']
     response = find_results(topic,type_of)
     return jsonify(response)

if __name__== '__main__':
    app.run(debug=True)
