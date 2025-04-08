from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        # Your chatbot's context
        context = """
        Welcome to Strategy Evolve. We offer online training for security professionals,
        AI tools, and business workflow consultancy.
        """

        # Send message to OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant. Use this context: {context}"},
                {"role": "user", "content": user_message}
            ]
        )

        # Return AI response
        return jsonify({"response": response.choices[0].message.content})
    
    except Exception as e:
        print("❌ ERROR:", str(e))  # Log error in Render logs
        return jsonify({"error": "Something went wrong on the server."}), 500

# Run server (Render will manage port automatically)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
