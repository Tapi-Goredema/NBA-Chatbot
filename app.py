from flask import Flask, request, jsonify
import pandas as pd
import requests

app = Flask(__name__)

# Load local CSV dataset
local_df = pd.read_csv('local_data.csv')

# BallDontLie API key & headers
API_KEY = "3756e490-28d6-4a44-9851-37b6e4757270"
HEADERS = {"Authorization": API_KEY}


@app.route('/')
def home():
    return "Chatbot is running. POST to /chat with JSON {\"message\": … }"


@app.route('/chat', methods=['POST'])
def chat():
    text = request.json.get('message', '').lower().strip()

    # — Local CSV queries —
    if "heaviest" in text:
        p = local_df.sort_values('Wt', ascending=False).iloc[0]
        return jsonify(response=f"Heaviest player: {p['Player']} at {p['Wt']} lbs.")
    if "college" in text:
        top = local_df['Colleges'].value_counts().idxmax()
        cnt = local_df['Colleges'].value_counts().max()
        return jsonify(response=f"Top college: {top} ({cnt} players)")

    # — Player Profile Info —
    if text.startswith("player info"):
        name_part = text.split("player info", 1)[1].strip()
        if not name_part:
            return jsonify(response="Please say “player info <first name> <last name>.”")

        tokens = name_part.split()
        if len(tokens) < 2:
            return jsonify(response="Please provide both first and last name.")

        first, last = tokens[0], tokens[-1]

        # lookup by first_name & last_name
        r = requests.get(
            "https://api.balldontlie.io/v1/players",
            params={"first_name": first, "last_name": last},
            headers=HEADERS
        )
        if r.status_code != 200:
            return jsonify(response="Player lookup failed.")
        data = r.json().get("data", [])
        if not data:
            return jsonify(response=f"No player found for '{name_part}'.")

        player = data[0]
        # extract profile fields
        num      = player.get("jersey_number", "N/A")
        college  = player.get("college",     "N/A")
        drafted  = f"{player.get('draft_year','?')} (Rd {player.get('draft_round','?')}, Pick {player.get('draft_number','?')})"

        resp = (
            f"{player['first_name']} {player['last_name']} — "
            f"#{num}, College: {college}, Draft: {drafted}."
        )
        return jsonify(response=resp)

    # — Fallback —
    return jsonify(response="Try “heaviest”, “college”, or “player info <first> <last>.”")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
