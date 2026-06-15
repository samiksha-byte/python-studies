from flask import Flask, render_template, request

app = Flask(__name__)

responses = {
    "hello": "Hello! Welcome to Campus Mood Bot.",
    "exam": "Revise important topics and practice daily.",
    "placement": "Practice coding and aptitude regularly.",
    "project": "Break your project into smaller tasks.",
    "python": "Python becomes easier with practice.",
    "java": "Java is widely used in enterprise applications.",
    "coding": "Practice coding every day.",
    "internship": "Build projects and improve your resume.",
    "resume": "Keep your resume simple and updated.",
    "library": "The library is a great place to learn.",
    "sports": "Sports improve mental and physical health.",
    "happy": "That's great. Keep smiling.",
    "sad": "Don't worry. Better days are coming.",
    "stressed": "Take a short break and relax.",
    "tired": "Get enough rest and stay hydrated.",
    "bye": "Goodbye. Have a nice day."
}

def get_reply(message):

    message = message.lower()

    if message in responses:
        return responses[message]

    return "Sorry, I don't understand that topic."

@app.route("/", methods=["GET", "POST"])
def home():

    reply = ""

    if request.method == "POST":
        message = request.form["message"]
        reply = get_reply(message)

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
