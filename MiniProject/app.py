from flask import Flask, render_template, request

app = Flask(__name__)

def get_reply(message):

    responses = {
        "hello": "Hi! Welcome to Campus Mood Bot.",
        "stressed": "Take a short break and come back stronger.",
        "tired": "Get some rest and stay hydrated.",
        "exam": "Revise important topics and practice previous questions.",
        "placement": "Practice coding and aptitude every day.",
        "project": "Break your project into smaller tasks.",
        "python": "Python becomes easier with regular practice.",
        "happy": "That's great! Keep smiling.",
        "sad": "Don't give up. Better days are coming.",
        "bye": "Goodbye! Have a productive day."
    }

    return responses.get(
        message.lower(),
        "Sorry, I don't have an answer for that."
    )

@app.route("/", methods=["GET", "POST"])
def home():

    reply = ""

    if request.method == "POST":
        message = request.form["message"]
        reply = get_reply(message)

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
