from flask import Flask, request, jsonify, make_response

from flask_cors import CORS


app = Flask(__name__)

CORS(app, origins=["https://tably.webflow.io"])


# Define your Python logic
def run_python_code(data):

    json_data = request.get_json()
    response = make_response(jsonify({"message": json_data}))
    response.headers['Access-Control-Allow-Origin'] = 'https://tably.webflow.io'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/execute', methods=['POST'])
def execute():
    try:
        # Parse the JSON payload
        json_data = request.get_json()
        # Process the input data (replace this with your logic)
        result = f"Received: {json_data}"
        
        # Create a response object with CORS headers
        response = make_response(jsonify({"message": result}))
        response.headers['Access-Control-Allow-Origin'] = 'https://tably.webflow.io'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    except Exception as e:
        response = make_response(jsonify({"error": str(e)}), 500)
        response.headers['Access-Control-Allow-Origin'] = 'https://tably.webflow.io'
        return response