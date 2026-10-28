from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)

app.secret_key = "guessing-game-secret"


difficulty_settings = {
    "easy": {"max_number": 10, "max_tries": 5},
    "medium": {"max_number": 50, "max_tries": 7},
    "hard": {"max_number": 100, "max_tries": 10}
}


@app.route("/")
def home():
    return render_template(
        "index.html",
        message="",
        message_type="",
        tries=session.get("tries", 0),
        max_number=session.get("max_number", 10),
        scores=session.get("scores", {
            "easy": 0,
            "medium": 0,
            "hard": 0
        })
    )


@app.route("/start", methods=["POST"])
def start_game():
    difficulty = request.form.get("difficulty", "easy")

    settings = difficulty_settings[difficulty]

    session["difficulty"] = difficulty
    session["max_number"] = settings["max_number"]
    session["max_tries"] = settings["max_tries"]

    if "scores" not in session:
        session["scores"] = {
            "easy": 0,
            "medium": 0,
            "hard": 0
        }

    session["secret"] = random.randint(1, settings["max_number"])
    session["tries"] = 0
    session["game_over"] = False

    return redirect("/")


@app.route("/guess", methods=["POST"])
def guess():
    if "secret" not in session or session.get("game_over"):
        return redirect("/")

    max_number = session["max_number"]
    max_tries = session["max_tries"]

    message = ""
    message_type = ""

    try:
        player_guess = int(request.form["guess"])
    except ValueError:
        message = "Please enter a valid number."
        message_type = "high"

        return render_template(
            "index.html",
            message=message,
            message_type=message_type,
            tries=session["tries"],
            max_number=max_number,
            scores=session.get("scores", {
                "easy": 0,
                "medium": 0,
                "hard": 0
            })
        )

    session["tries"] += 1

    print("Player guessed:", player_guess)
    print("Secret number:", session["secret"])
    print("Tries:", session["tries"])

    if player_guess < 1 or player_guess > max_number:
        message = "Out of range! 😞"

    elif player_guess == session["secret"]:

        base_scores = {
            "easy": 10,
            "medium": 20,
            "hard": 30
        }

        difficulty = session["difficulty"]

        base_score = base_scores[difficulty]

        score = base_score - ((session["tries"] - 1) * 2)

        if score < 1:
            score = 1

        session["scores"][difficulty] += score

        session.modified = True

        message = (
            f"You got it! 🎉🔥 in {session['tries']} tries "
            f"(+{score} points)"
        )

        message_type = "win"
        session["game_over"] = True

    elif session["tries"] >= max_tries:
        message = f"You lost! 😓 The number was {session['secret']}"
        message_type = "lose"
        session["game_over"] = True

    elif player_guess > session["secret"]:
        message = "Too high! 🤔"
        message_type = "high"

    elif player_guess < session["secret"]:
        message = "Too low! 🤔"
        message_type = "low"

    print("Result:", message)

    return render_template(
        "index.html",
        message=message,
        message_type=message_type,
        tries=session["tries"],
        max_number=max_number,
        scores=session.get("scores", {
            "easy": 0,
            "medium": 0,
            "hard": 0
        })
    )

@app.route("/reset")
def reset():
    difficulty = session.get("difficulty", "easy")

    settings = difficulty_settings[difficulty]

    session["secret"] = random.randint(1, settings["max_number"])
    session["tries"] = 0
    session["game_over"] = False

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)