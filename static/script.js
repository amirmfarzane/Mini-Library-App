function loadBooks() {
    fetch("/books")
        .then(res => res.json())
        .then(books => {
            const list = document.getElementById("booksList");
            list.innerHTML = "";
            if (books.length === 0) {
                list.innerHTML = "<p>No books in the library yet.</p>";
                return;
            }
            books.forEach(book => {
                const div = document.createElement("div");
                div.className = "book-item";
                div.innerHTML = `
                    <span><strong>${book.title}</strong> by ${book.author} (${book.year})</span>
                    <button class="delete-btn" onclick="deleteBook(${book.id})">Delete</button>
                `;
                list.appendChild(div);
            });
        });
}

function addBook() {
    const title = document.getElementById("title").value.trim();
    const author = document.getElementById("author").value.trim();
    const year = document.getElementById("year").value.trim();

    if (!title || !author || !year) {
        alert("Please fill in all fields!");
        return;
    }

    fetch("/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, author, year })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            document.getElementById("title").value = "";
            document.getElementById("author").value = "";
            document.getElementById("year").value = "";
            loadBooks();
        }
    });
}

function deleteBook(id) {
    if (!confirm("Are you sure you want to delete this book?")) return;

    fetch(`/delete/${id}`, { method: "DELETE" })
        .then(() => loadBooks());
}

function searchBooks() {
    const query = document.getElementById("searchInput").value;
    if (query === "") {
        loadBooks();
        return;
    }

    fetch(`/search?q=${encodeURIComponent(query)}`)
        .then(res => res.json())
        .then(books => {
            const list = document.getElementById("booksList");
            list.innerHTML = "";
            if (books.length === 0) {
                list.innerHTML = "<p>No books found.</p>";
                return;
            }
            books.forEach(book => {
                const div = document.createElement("div");
                div.className = "book-item";
                div.innerHTML = `
                    <span><strong>${book.title}</strong> by ${book.author} (${book.year})</span>
                    <button class="delete-btn" onclick="deleteBook(${book.id})">Delete</button>
                `;
                list.appendChild(div);
            });
        });
}

// Load books when page opens
loadBooks();