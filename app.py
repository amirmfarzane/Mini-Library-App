from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
BOOKS_FILE = "books.json"

def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/books")
def get_books():
    return jsonify(load_books())

@app.route("/add", methods=["POST"])
def add_book():
    data = request.json
    books = load_books()
    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"],
        "year": data["year"]
    }
    books.append(new_book)
    save_books(books)
    return jsonify({"success": True, "book": new_book})

@app.route("/delete/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    books = load_books()
    books = [b for b in books if b["id"] != book_id]
    # Re-index IDs
    for i, b in enumerate(books):
        b["id"] = i + 1
    save_books(books)
    return jsonify({"success": True})

@app.route("/search")
def search():
    query = request.args.get("q", "").lower()
    books = load_books()
    results = [b for b in books if query in b["title"].lower()]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)