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

def delete_book(books):
    list_books(books)
    if not books:
        return
    try:
        book_id = int(input("Enter book ID to delete: "))
        for b in books:
            if b["id"] == book_id:
                books.remove(b)
                save_books(books)
                print("Book deleted!")
                return
        print("Book not found.")
    except:
        print("Invalid ID.")

def list_books(books):
    if not books:
        print("No books in library.")
        return
    for b in books:
        print(f"{b['id']}: {b['title']} - {b['author']} ({b['year']})")

# Test update
if __name__ == "__main__":
    books = load_books()
    print("\n--- List ---")
    list_books(books)