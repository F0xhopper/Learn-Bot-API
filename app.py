from flask import Flask
from openai import OpenAI
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


client = OpenAI(
    
    api_key=("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"),
)
# give books, docs , pods , yt vids

def CustomChatGPTbooks(user_input):
    Book_response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
    {"role": "system", "content": "just give a list of the best books to learn about the given subject"},
    {"role": "user", "content": user_input}
  ]
    )

    ChatGPT_reply = [Book_response.choices[0].message.content]
    split_response = ChatGPT_reply[0].split('\n') 
  
    return split_response


