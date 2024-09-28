import uuid
from pydantic import BaseModel


class BookSchema(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    testing: str
 
class NewBookSchema(BaseModel): 
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str
    testing: str

class BookUpdateSchema(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str