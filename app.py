import os
import sys
from flask import Flask

# Print startup message to stderr (visible in docker logs)
print(">>> Starting Flask app...", file=sys.stderr)

app = Flask(__name__)

@app.route('/')
def home():
    message = os.getenv('APP_MESSAGE', 'Default message')
    print(f">>> Home route called, returning: {message}", file=sys.stderr)
    return message

@app.route('/health')
def health():
    health_status = os.getenv('APP_HEALTH', 'healthy')
    print(f">>> Health route called, returning: {health_status}", file=sys.stderr)
    return health_status

if __name__ == '__main__':
    print(">>> Running on http://0.0.0.0:5000", file=sys.stderr)
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f">>> CRASH: {e}", file=sys.stderr)
        raise