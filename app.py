# app.py
from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Sample stories
stories = [
    "Once upon a time, there was a cat.",
    "In a faraway land, a brave knight saved the day.",
    "A little bird flew across the blue sky."
]

# API endpoint to get stories
@app.route('/api/stories', methods=['GET'])
def get_stories():
    return jsonify(stories)

if __name__ == "__main__":
    # Use environment variables for the host and port for deployment on Vercel
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host=host, port=port)
