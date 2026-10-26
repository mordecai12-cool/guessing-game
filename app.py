from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)

app.secret_key = "guessing-game-secret"

@app.route("/", methods=["GET", "POST"])
def home():
    if "secret" not in session:
        session["difficulty"] = "easy"
        session["max_number"] = 10
        session["max_tries"] = 5

        session["secret"] = random.randint(1, session["max_number"])
        session["tries"] = 0
        session["game_over"] = False

    message = ""
    message_type = ""
    difficulty_settings = {
        "easy": {"max_number": 10, "max_tries": 5},
        "medium": {"max_number": 50, "max_tries": 7},
        "hard": {"max_number": 100, "max_tries": 10}
    }

    if request.method == "POST" and not session["game_over"]:
        difficulty = request.form.get("difficulty", "easy")

        settings = difficulty_settings[difficulty]

        session["difficulty"] = difficulty
        session["max_number"] = settings["max_number"]
        session["max_tries"] = settings["max_tries"]

        max_number = session["max_number"]
        max_tries = session["max_tries"]

        if session["tries"] == 0:
            session["secret"] = random.randint(1, max_number)

        try:
            guess = int(request.form["guess"])
        except ValueError:
            message = "Please enter a valid number."
            message_type = "high"
            return render_template(
                "index.html",
                message=message,
                tries=session["tries"],
                message_type=message_type
            )
        session["tries"] += 1

        print("Player guessed:", guess)
        print("Secret number:", session["secret"])
        print("Tries:", session["tries"])

        if guess < 1 or guess > max_number:
            message = "Out of range! 😞"

        elif guess == session["secret"]:
            message = f"You got it! 🎉🔥 in {session['tries']} tries"
            message_type = "win"
            session["game_over"] = True

        elif session["tries"] >= max_tries:
            message = f"You lost! 😓 The number was {session['secret']}"
            message_type = "lose"
            session["game_over"] = True

        elif guess > session["secret"]:
            message = "Too high! 🤔"
            message_type = "high"

        elif guess < session["secret"]:
            message = "Too low! 🤔"
            message_type = "low"

        print("Result:", message)

    return render_template(
        "index.html",
        message=message,
        tries=session["tries"],
        message_type=message_type,
        max_number=session["max_number"]
    )

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)