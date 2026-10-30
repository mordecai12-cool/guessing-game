# 🎯 Guess The Number

A simple and interactive **number guessing game** built with **Python and Flask**.

The player chooses a difficulty level, enters guesses, receives hints, earns points for winning, and can track their game statistics and history.

## 🚀 Features

- 👤 Player name
- 🎯 Three difficulty levels:
  - Easy — numbers 1–10, 5 tries
  - Medium — numbers 1–50, 7 tries
  - Hard — numbers 1–100, 10 tries
- 🤔 Too high / Too low hints
- ❌ Out-of-range validation
- 🏆 Score system
- 🥇 Best score for each difficulty
- 📊 Player statistics
  - Games played
  - Wins
  - Losses
  - Win rate
- 📜 Game history
- 🗑️ Clear game history
- 🔄 Play Again option
- 📱 Responsive design
- 🔐 Session-based game state
- ⚡ Production server support with Gunicorn

## 🛠️ Technologies

- Python
- Flask
- HTML
- CSS
- JavaScript
- Gunicorn
- python-dotenv

## 📁 Project Structure

```text
guessing-game/
│
├── app.py
├── .env
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── venv/
```

> The `venv/` folder and `.env` file are ignored by Git and should not be uploaded to GitHub.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/mordecai12-cool/guessing-game.git
cd guessing-game
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install flask python-dotenv gunicorn
```

### 5. Create the environment file

Create a `.env` file in the project root:

```text
SECRET_KEY=your-secret-key
```

Use a strong, private secret key and never commit the `.env` file to GitHub.

## ▶️ Run Locally

For development:

```bash
python3 app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## 🚀 Run with Gunicorn

For production-style testing:

```bash
gunicorn app:app
```

The application will normally be available at:

```text
http://127.0.0.1:8000
```

## 🎮 How to Play

1. Enter your name.
2. Choose a difficulty.
3. Start the game.
4. Enter a number within the displayed range.
5. Use the hints to adjust your next guess.
6. Try to find the secret number before your attempts run out.
7. Win games to earn points and improve your best score.

## 🏆 Scoring

Each difficulty has a different starting score:

| Difficulty | Starting Score |
|---|---:|
| Easy | 10 |
| Medium | 20 |
| Hard | 30 |

Two points are deducted for each additional guess.

A winning score will never go below **1 point**.

A lost game gives **0 points**.

## 📊 Statistics

The game tracks:

- Total completed games
- Wins
- Losses
- Win rate
- Total accumulated points
- Best score for each difficulty
- Previous game results

## 🔐 Security

The Flask secret key is stored in an environment variable rather than directly in the source code.

The `.env` file is excluded from Git using `.gitignore`.

Debug mode is disabled for production.

## 👨‍💻 Author

**Mordecai Marvellous**

Built as a Python/Flask learning project.# 🎯 Guess The Number

A simple and interactive **number guessing game** built with **Python and Flask**.

The player chooses a difficulty level, enters guesses, receives hints, earns points for winning, and can track their game statistics and history.

## 🚀 Features

- 👤 Player name
- 🎯 Three difficulty levels:
  - Easy — numbers 1–10, 5 tries
  - Medium — numbers 1–50, 7 tries
  - Hard — numbers 1–100, 10 tries
- 🤔 Too high / Too low hints
- ❌ Out-of-range validation
- 🏆 Score system
- 🥇 Best score for each difficulty
- 📊 Player statistics
  - Games played
  - Wins
  - Losses
  - Win rate
- 📜 Game history
- 🗑️ Clear game history
- 🔄 Play Again option
- 📱 Responsive design
- 🔐 Session-based game state
- ⚡ Production server support with Gunicorn

## 🛠️ Technologies

- Python
- Flask
- HTML
- CSS
- JavaScript
- Gunicorn
- python-dotenv

## 📁 Project Structure

```text
guessing-game/
│
├── app.py
├── .env
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── venv/
```

> The `venv/` folder and `.env` file are ignored by Git and should not be uploaded to GitHub.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/mordecai12-cool/guessing-game.git
cd guessing-game
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install flask python-dotenv gunicorn
```

### 5. Create the environment file

Create a `.env` file in the project root:

```text
SECRET_KEY=your-secret-key
```

Use a strong, private secret key and never commit the `.env` file to GitHub.

## ▶️ Run Locally

For development:

```bash
python3 app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## 🚀 Run with Gunicorn

For production-style testing:

```bash
gunicorn app:app
```

The application will normally be available at:

```text
http://127.0.0.1:8000
```

## 🎮 How to Play

1. Enter your name.
2. Choose a difficulty.
3. Start the game.
4. Enter a number within the displayed range.
5. Use the hints to adjust your next guess.
6. Try to find the secret number before your attempts run out.
7. Win games to earn points and improve your best score.

## 🏆 Scoring

Each difficulty has a different starting score:

| Difficulty | Starting Score |
|---|---:|
| Easy | 10 |
| Medium | 20 |
| Hard | 30 |

Two points are deducted for each additional guess.

A winning score will never go below **1 point**.

A lost game gives **0 points**.

## 📊 Statistics

The game tracks:

- Total completed games
- Wins
- Losses
- Win rate
- Total accumulated points
- Best score for each difficulty
- Previous game results

## 🔐 Security

The Flask secret key is stored in an environment variable rather than directly in the source code.

The `.env` file is excluded from Git using `.gitignore`.

Debug mode is disabled for production.

## 👨‍💻 Author

**Mordecai Otit Marvellous**

Built as a Python/Flask learning project.