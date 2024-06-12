This Flask application allows users to send POST requests to get recommendations for resources (e.g., books, articles) on a specific topic using the OpenAI Chat API.

Features

- Cross-Origin Resource Sharing (CORS): Enabled for handling requests from different origins.
- OpenAI API Integration: Uses OpenAI's Chat API to fetch recommendations.
- Simple JSON API: Receives topic and type of resource via POST request and returns a list of recommendations.

Usage

Clone repo:

git clone https://github.com/F0xhopper/Learn-Bot-API

Go into app:

cd flask-openai-app

Install dependencies:

pip install -r requirements.txt

Set OPENAI API key:

API_KEY=your_openai_api_key
