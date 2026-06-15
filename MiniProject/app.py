from flask import Flask, render_template, request

app = Flask(__name__)

chat_responses = {
    "hello": "Hi! Welcome to Random Chat Project.",
    "how are you": "I am doing great.",
    "python": "Python is easy and powerful.",
    "college": "College life is fun and educational.",
    "bye": "Goodbye! Have a nice day."
}

def get_reply(message):
    message = message.lower()

    if message in chat_responses:
        return chat_responses[message]

    return "Sorry, I don't understand that."

@app.route("/", methods=["GET", "POST"])
def home():

    reply = ""

    if request.method == "POST":
        user_message = request.form["message"]
        reply = get_reply(user_message)

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
