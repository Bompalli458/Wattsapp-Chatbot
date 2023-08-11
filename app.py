from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the incoming JSON payload from Gupshup
    incoming_data = request.get_json()

    # Extract the user's message from the payload
    user_message = incoming_data.get('text')

    # Process the user's message using your Rasa chatbot logic here
    # For example, you can call your Rasa model to get the chatbot's response

    # Replace the placeholder response with your chatbot's actual response
    bot_response = "Hello, I am your Rasa-powered chatbot! You said: " + user_message

    # Prepare the response in the required format (e.g., JSON)
    response_data = {
        "text": bot_response,
        # You can add other fields to customize the response based on Gupshup's requirements
    }

    # Convert the response data to JSON and send it back to Gupshup
    return jsonify(response_data)
if __name__ == '__main__':
    app.run(host='192.168.0.148', port=5058)

