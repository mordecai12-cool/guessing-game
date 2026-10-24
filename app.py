from flask import Flask, render_template, request, session
import random

app = Flask(__name__)

app.secret_key = "guessing-game-secret"

@app.route("/", methods=["GET", "POST"])
def home():
    if "secret" not in session or "game_over" not in session:
        session["secret"] = random.randint(1, 10)
        session["tries"] = 0
        session["game_over"] = False

    message = ""

    if request.method == "POST" and not session["game_over"]:
        guess = int(request.form["guess"])
        session["tries"] += 1

        print("Player guessed:", guess)
        print("Secret number:", session["secret"])
        print("Tries:", session["tries"])

        if guess < 1 or guess > 10:
            message = "Out of range! 😞"

        elif guess == session["secret"]:
            message = f"You got it! 🥳👍 in {session['tries']} tries"
            session["game_over"] = True

        elif session["tries"] >= 5:
            message = f"You lost! 😓 The number was {session['secret']}"
            session["game_over"] = True

        elif guess > session["secret"]:
            message = "Too high! 🤔"

        elif guess < session["secret"]:
            message = "Too low! 🤔"

        print("Result:", message)

    return render_template(
        "index.html",
        message=message,
        tries=session["tries"]
    )

if __name__ == "__main__":
    app.run(debug=True)