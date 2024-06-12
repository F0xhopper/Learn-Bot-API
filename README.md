This Flask application allows users to send POST requests to get recommendations for resources (e.g., books, articles) on a specific topic using the OpenAI Chat API.

Features

- Cross-Origin Resource Sharing (CORS): Enabled for handling requests from different origins.
- OpenAI API Integration: Uses OpenAI's Chat API to fetch recommendations.
- Simple JSON API: Receives topic and type of resource via POST request and returns a list of recommendations.

Usage

git clone https://github.com/your-repo/flask-openai-app.git

cd flask-openai-app

pip install -r requirements.txt
