import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("J. R. R. Tolkien")
author_repository.save(author_1)

author_2 = Author("J.K. Rowling")
author_repository.save(author_2)

author_repository.select_all()

book_1 = Book("The Lord of the Rings", "fantasy", author_1)
book_repository.save(book_1)

book_2 = Book("Harry Potter and the Philosopher's Stone", "fantasy", author_2)
book_repository.save(book_2)

book_repository.select_all()

pdb.set_trace()
