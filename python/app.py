from flask import Flask, jsonify, send_from_directory
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
app = Flask(__name__, static_folder=str(ROOT / "website"), static_url_path="")

@app.get("/")
def home():
    return send_from_directory(ROOT / "website", "index.html")

@app.get("/api/accidents")
def accidents():
    rows = []
    with open(ROOT / "data" / "state_accidents_2020_2024.csv", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            for year in ("2020","2021","2022","2023","2024"):
                row[year] = int(row[year]) if row[year] not in ("", "NA", "None") else None
            rows.append(row)
    totals = {"2020":372181,"2021":412432,"2022":461312,"2023":480583,"2024":487705}
    return jsonify({"years":[2020,2021,2022,2023,2024], "totals":totals, "states":rows})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
