from flask import Flask, render_template, request
from src.hyderabad_navigator import chatbot_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_query = request.form.get("query", "")
        if user_query.strip():
            response = chatbot_response(user_query)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
