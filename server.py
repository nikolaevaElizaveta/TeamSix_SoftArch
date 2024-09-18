from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# List to store messages
messages = []


@app.route('/messages', methods=['POST'])
def post_message():
    """Endpoint for posting a new message."""
    message = request.json.get('message', '')
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    messages.append({'message': message, 'timestamp': timestamp})
    return jsonify({'status': 'Message received', 'message': message, 'timestamp': timestamp}), 200


@app.route('/messages', methods=['GET'])
def get_messages():
    """Endpoint to get all messages."""
    return jsonify({'messages': messages}), 200


@app.route('/messages/count', methods=['GET'])
def get_message_count():
    """Endpoint to get the total number of messages."""
    return jsonify({'count': len(messages)}), 200


@app.route('/messages/latest', methods=['GET'])
def get_latest_message():
    """Endpoint to get the latest message."""
    if messages:
        latest_message = messages[-1]
        return jsonify(latest_message), 200
    else:
        return jsonify({"error": "No messages available"}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
