from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS, cross_origin
import os

# Initialize Flask app
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Initialize OpenAI client with API key from environment variable
client = OpenAI(
    api_key=(os.environ.get('API_KEY')),
)

# Function to find results using OpenAI Chat API
def find_results(topic, type):
    raw_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"just give a list of the best {type} to learn about the given subject"},
            {"role": "user", "content": topic}
        ]
    )

    # Extract and process the response
    openai_reply = [raw_response.choices[0].message.content]
    split_response = openai_reply[0].split('\n')
    send = []
    for response in split_response:
        if len(response) != 0 and response[0].isnumeric():
            send.append(response)
    
    # If no valid response is found, return a default message
    if send == []:
        send = [f'Sorry we could not find any {type} on {topic}']
    
    return send

# Endpoint to handle POST requests
@app.route('/post', methods=["POST"])
@cross_origin()
def send():
    # Parse JSON input from POST request
    input_json = request.get_json(force=True) 
    topic = input_json['topic']
    type_of = input_json['type']
    
    # Call function to find results based on input
    response = find_results(topic, type_of)
    
    # Return JSON response
    return jsonify(response)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)