from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'GreyMatters'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) # Heroku provides the port
    app.run(host='0.0.0.0', port=port)
