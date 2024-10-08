from typing import List
from fastapi import APIRouter, status, Depends
from src.auth.dependencies import AccessTokenBearer
from src.books.book_data import books
from src.books.schemas import BookSchema as Book, BookUpdateSchema as BookUpdateModel, NewBookSchema
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from src.books.service import BookService
from src.db.main import get_session

book_router = APIRouter()
book_service = BookService()
acccess_token_bearer = AccessTokenBearer()




@book_router.get("/books", response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session), token_details=Depends(acccess_token_bearer)):
    books = await book_service.get_all_books(session)
    return books


@book_router.post("/books", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(
    book_data: NewBookSchema, session: AsyncSession = Depends(get_session),
    token_details=Depends(acccess_token_bearer)
):
    new_book = await book_service.create_book(book_data, session)

    return new_book


@book_router.get("/book/{book_id}", response_model=Book)
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session), token_details=Depends(acccess_token_bearer)):
    book = await book_service.get_book(book_uid, session)
   
    if book:
        return book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )


@book_router.patch("/book/{book_id}", response_model=Book)
async def update_book(
    book_uid: str,
    book_update_data: BookUpdateModel,
    session: AsyncSession = Depends(get_session),
    token_details=Depends(acccess_token_bearer)
):
    
    updated_book = await book_service.update_book(book_uid, book_update_data, session)

    if updated_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    else:
        return updated_book


@book_router.delete("/book/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid: str, session: AsyncSession = Depends(get_session), token_details=Depends(acccess_token_bearer)):
    
    book_to_delete = await book_service.delete_book(book_uid, session)
    
    if book_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    else:

        return {}