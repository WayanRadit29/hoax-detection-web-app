import sqlite3
from flask import Flask, render_template, request
from prediction import predict_hoax

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    result = None
    input_text = ""

    if request.method == "POST":
        input_text = request.form.get("text", "").strip()

        if input_text:
            result = predict_hoax(input_text)

    return render_template(
        "prediction.html",
        result=result,
        input_text=input_text
    )


@app.route("/information")
def information():
    source = request.args.get("source", "")
    topic = request.args.get("topic", "")
    label = request.args.get("label", "")
    start_date = request.args.get("start_date", "")
    end_date = request.args.get("end_date", "")

    connection = get_db_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM information WHERE 1=1"
    params = []

    if source:
        query += " AND source = ?"
        params.append(source)

    if topic:
        query += " AND topic = ?"
        params.append(topic)

    if label:
        query += " AND label = ?"
        params.append(label)

    if start_date:
        query += " AND publication_date >= ?"
        params.append(start_date)

    if end_date:
        query += " AND publication_date <= ?"
        params.append(end_date)

    query += " ORDER BY publication_date DESC LIMIT 100"

    cursor.execute(query, params)
    information_data = cursor.fetchall()

    cursor.execute("SELECT DISTINCT source FROM information ORDER BY source")
    sources = cursor.fetchall()

    cursor.execute("SELECT DISTINCT topic FROM information ORDER BY topic")
    topics = cursor.fetchall()

    connection.close()

    return render_template(
        "information.html",
        information_data=information_data,
        sources=sources,
        topics=topics,
        selected_source=source,
        selected_topic=topic,
        selected_label=label,
        selected_start_date=start_date,
        selected_end_date=end_date
    )


if __name__ == "__main__":
    app.run(debug=True)