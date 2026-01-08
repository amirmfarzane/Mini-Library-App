import json
import os

BOOKS_FILE = "books.json"

def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


def add_book(books):
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year: ")
    book = {"id": len(books) + 1, "title": title, "author": author, "year": year}
    books.append(book)
    save_books(books)
    print("Book added!")

if __name__ == "__main__":
    books = load_books()
    add_book(books)