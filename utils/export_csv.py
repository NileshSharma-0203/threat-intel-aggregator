import sqlite3
import csv

def export_to_csv(db_path='database/leaks.db', output_file='leaks_export.csv'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT id, url, keyword, snippet, timestamp FROM leaks")
    rows = cursor.fetchall()

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'URL', 'Keyword', 'Snippet', 'Timestamp'])
        writer.writerows(rows)

    conn.close()
    print(f"✅ Exported {len(rows)} leaks to {output_file}")

if __name__ == "__main__":
    export_to_csv()
