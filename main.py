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

def search_books(books):
    query = input("Search by title: ").lower()
    results = [b for b in books if query in b["title"].lower()]
    if results:
        for b in results:
            print(f"{b['id']}: {b['title']} - {b['author']} ({b['year']})")
    else:
        print("No books found.")

def main():
    books = load_books()
    while True:
        print("\n=== Mini Library App ===")
        print("1. Add book")
        print("2. Delete book")
        print("3. Search")
        print("4. List all")
        print("5. Exit")
        choice = input("Choose: ")
        if choice == "1": add_book(books)
        elif choice == "2": delete_book(books)
        elif choice == "3": search_books(books)
        elif choice == "4": list_books(books)
        elif choice == "5": break

if __name__ == "__main__":
    main()

# Conflict test - version from conflict-test branch (conflict producer)

# Conflict test - version from main branch (different text)