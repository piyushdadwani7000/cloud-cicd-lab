from flask import Flask, jsonify, request

app = Flask(__name__)


# Root route
@app.route("/")
def home():
    return "<h1>Flask App is Running!</h1><p>Visit /api/hello or /greet/YourName</p>"


# Dynamic URL parameter route
@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"


# JSON API endpoint supporting GET and POST
@app.route("/api/hello", methods=["GET", "POST"])
def api_hello():
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        user = data.get("name", "Anonymous")
        return jsonify(
            {
                "status": "success",
                "message": f"Data received for {user}",
                "payload": data,
            }
        ), 200

    return jsonify({"status": "success", "message": "Hello from Flask API!"}), 200


if __name__ == "__main__":
    # Runs local development server on http://127.0.0.1:5000
    app.run(debug=True, host="0.0.0.0", port=5000)
