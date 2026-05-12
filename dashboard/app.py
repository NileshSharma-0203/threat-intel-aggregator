from flask import Flask, render_template, request, send_file
import sqlite3
import csv
import os

app = Flask(__name__)
DB_PATH = os.path.join("data", "leaks.db")

def get_leaks(search=""):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    if search:
        query = f"""
            SELECT id, url, leak_type, content_snippet, timestamp 
            FROM leaks 
            WHERE url LIKE ? OR leak_type LIKE ? OR content_snippet LIKE ? 
            ORDER BY timestamp DESC
        """
        search_term = f"%{search}%"
        cursor.execute(query, (search_term, search_term, search_term))
    else:
        cursor.execute("""
            SELECT id, url, leak_type, content_snippet, timestamp 
            FROM leaks 
            ORDER BY timestamp DESC
        """)
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route("/")
def index():
    search = request.args.get("search", "")
    leaks = get_leaks(search)
    return render_template("index.html", leaks=leaks, search=search)

@app.route("/download")
def download_csv():
    rows = get_leaks()
    filepath = "leaks_export.csv"
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "URL", "Leak Type", "Snippet", "Timestamp"])
        for row in rows:
            writer.writerow(row)
    return send_file(filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=False)
