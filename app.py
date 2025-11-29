import os
import threading
import asyncio
from flask import Flask, jsonify
from main import StarTinG 

# Create the Flask app
app = Flask(__name__)

# Read the PORT environment variable provided by Render
PORT = int(os.environ.get('PORT', 5000))

# 1. Route for Health Check and Port Scan
@app.route('/')
def health_check():
    # This endpoint satisfies Render's port scan and health check
    return jsonify({
        "status": "running", 
        "service": "Web Service (Bot Core Running in Background)"
    })

# 2. Function to start the bot's core logic
def start_bot_core():
    # Start the async function from main.py
    print(f"Starting Bot Core in background thread...")
    asyncio.run(StarTinG())

# 3. Start the application
if __name__ == '__main__':
    # Start the bot core in a separate background thread (daemon=True ensures it stops when Flask stops)
    bot_thread = threading.Thread(target=start_bot_core, daemon=True)
    bot_thread.start()
    
    # Run the Flask app on the host 0.0.0.0 and the port provided by Render
    print(f"Flask Web Server listening on port {PORT} for Render Health Check...")
    # Use Gunicorn to run in production, but app.run for local testing is fine.
    # For Render, the final Start Command will use gunicorn.
    app.run(host='0.0.0.0', port=PORT)