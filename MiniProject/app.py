from flask import Flask, render_template, request

app = Flask(__name__)

responses = {

    "hello": "Hello! Welcome to Campus Mood Bot.",

    "exam": "Create a study plan and revise important topics daily.",

    "placement": "Practice coding, aptitude and communication skills regularly.",

    "project": "Divide your project into smaller tasks and complete them one by one.",

    "python": "Python is easy to learn when you practice every day.",

    "java": "Java is widely used in enterprise applications.",

    "coding": "Consistency is the key to becoming a good programmer.",

    "internship": "Build projects and improve your resume to get internships.",

    "resume": "Keep your resume simple, clean and updated.",

    "attendance": "Regular attendance helps you understand concepts better.",

    "library": "The library is a great place for focused learning.",

    "sports": "Sports improve both physical and mental health.",

    "hostel": "Hostel life teaches independence and responsibility.",

    "friends": "Good friends support and motivate each other.",

    "happy": "That's wonderful! Keep spreading positivity.",

    "sad": "Every difficult phase will pass. Stay strong.",

    "stressed": "Take a short break and come back refreshed.",

    "tired": "Get enough sleep and stay hydrated.",

    "motivation": "Small progress every day leads to big success.",

    "bye": "Goodbye! Have a productive day."
}

def get_reply(user_message):

    user_message = user_message.lower().strip()

    if user_message in responses:
        return responses[user_message]

    return "Sorry, I don't have information about that topic."


@app.route("/", methods=["GET", "POST"])
def home():

    reply = ""

    if request.method == "POST":

        message = request.form["message"]

        reply = get_reply(message)

    return render_template("index.html", reply=reply)


if __name__ == "__main__":
    app.run(debug=True)
