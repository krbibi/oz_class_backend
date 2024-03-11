from fastapi import APIRouter,HTTPException
from uuid import uuid4, UUID
from models import Book, CreateBook, SearchResultBook
from typing import List

route = APIRouter()
books: List[Book] = []


# fetch('api/v1/books', data={'title':'제목', 'author':'저자'})
# api/v1/books [POST]
@route.post('/')
def create_book(book_data: CreateBook) -> Book:
    book = Book(id=uuid4(), **book_data.model_dump())
    books.append(book)

    return book

@route.get('/{book_id}')
def get_book_id(book_id: UUID) -> Book:
    book = next((book for book in books if book.id == book_id), None)

    if not book:
            raise HTTPException(status_code=404)
    return book

from typing import Optional

# pathParm => {book_id}
# queryParam => search?keyword=blahblah
@route.get('/search/')
def search_book(keyword: Optional[str], 
                max_results: int = 10) -> SearchResultBook:
     
     result = [book for book in books if keyword in book.title ] if keyword else books

     # [for book in books:
     # if book.title in keyword:
     #      book]
     #
     #
     return SearchResultBook(results=result[:max_results])

