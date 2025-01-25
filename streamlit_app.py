from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)

CORS(app, origins=["https://tably.webflow.io"])


# Define your Python logic
def run_python_code(data):
    # Perform operations with the submitted data
    return f"You submitted: {data}"

@app.route('/execute', methods=['POST'])
def execute():
    # Get form data sent by Webflow
    user_input = request.form.get('input')
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    
    result = run_python_code(user_input)
    return jsonify({"message": result})
