# 📚 Book Collection Manager

A Python-based CLI application to manage a personal book collection, allowing users to add, remove, search, update, and track their reading progress.

## 🚀 Features
- Add new books with details (title, author, genre, year, and read status)
- Remove books by title
- Search for books by title or author
- Update book details
- View all books in the collection
- Track reading progress with completion statistics
- Store book data persistently in `books_data.json`

## 🛠 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/book-collection-manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd book-collection-manager
   ```
3. Install dependencies (if needed, though this script runs with core Python libraries):
   ```bash
   pip install -r requirements.txt  # If any dependencies exist
   ```
4. Run the script:
   ```bash
   python book_manager.py
   ```

## 📌 Usage
Run the script and interact with the menu:
```bash
📚 Welcome to Your Book Collection Manager! 📚
1. Add a new book
2. Remove a book
3. Search for books
4. Update book details
5. View all books
6. View reading progress
7. Exit
```
### Example: Adding a Book
```
Enter book title: The Great Gatsby
Enter author: F. Scott Fitzgerald
Enter publication year: 1925
Enter genre: Fiction
Have you read this book? (yes/no): yes
```
✅ Book added successfully!

### 📜 Viewing Reading Progress
Displays the total books and the percentage of books read.

## 📂 Data Storage
- Books are saved in `books_data.json`.
- Each book entry follows this format:
  ```json
  {
      "title": "1984",
      "author": "George Orwell",
      "year": "1949",
      "genre": "Dystopian",
      "read": true
  }
  ```

## 🛠 Troubleshooting
- **Book not saving?** Ensure `books_data.json` exists and has write permissions.
- **Data not loading?** Check if the JSON file is correctly formatted.

## 📜 License
This project is open-source and available under the MIT License.

