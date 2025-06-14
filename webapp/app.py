from flask import Flask, jsonify
import socket
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    hostname = socket.gethostname()
    logging.info(f"Accessed by client at '/' - Hostname: {hostname}")
    return f"✅ Hello from Flask App running inside Kubernetes Pods! \nHostname: {hostname}"

@app.route("/health")
def health():
    return jsonify(status="UP"), 200

@app.route("/info")
def info():
    return jsonify(
        service="Flask Docker App via Ansible",
        author="Priyam Sanodiya",
        host=socket.gethostname()
    )

if __name__ == "__main__":
    # Run on 0.0.0.0 to expose publicly, not just localhost
    app.run(host="0.0.0.0", port=5000)
