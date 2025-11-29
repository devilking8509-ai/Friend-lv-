import os
import threading
import asyncio
import sys
import time
from flask import Flask, jsonify
from main import StarTinG 

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 5000))

# ग्लोबल वेरिएबल बॉट का स्टेटस चेक करने के लिए
bot_status = "Not Started"

def start_bot_core():
    global bot_status
    print("--- BOT THREAD STARTED ---")
    try:
        # यह लूप बॉट को क्रैश होने पर दोबारा चालू करेगा
        while True:
            print("Running StarTinG()...")
            bot_status = "Running"
            asyncio.run(StarTinG())
            print("Bot crashed or stopped! Restarting in 10 seconds...")
            bot_status = "Crashed/Restarting"
            time.sleep(10)
    except Exception as e:
        print(f"CRITICAL ERROR IN BOT THREAD: {e}")
        bot_status = f"Error: {str(e)}"
        # Error को कंसोल में प्रिंट करें ताकि Logs में दिखे
        sys.stdout.flush()

@app.route('/')
def health_check():
    return jsonify({
        "status": "Online", 
        "bot_internal_status": bot_status,
        "service": "Free Fire Bot Service"
    })

if __name__ == '__main__':
    # थ्रेड स्टार्ट करें
    bot_thread = threading.Thread(target=start_bot_core, daemon=True)
    bot_thread.start()
    
    # Flask सर्वर स्टार्ट करें
    print(f"Flask Web Server running on port {PORT}")
    app.run(host='0.0.0.0', port=PORT)
