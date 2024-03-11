from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: Optional[str] = None

# Create
class CreateBook(BaseModel):
    title: str
    author: str
    description: Optional[str] = None


# Search
class BookSearch(BaseModel):
    results: Optional[Book]

from typing import List
class SearchResultBook(BaseModel):
    results: List[Book]
