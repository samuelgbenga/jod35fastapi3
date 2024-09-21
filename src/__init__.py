from fastapi import FastAPI

from src.books.routes import book_router

from src.db.main import initdb

from contextlib import asynccontextmanager


version = 'v1'

#the lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):    
    print("Server is starting...")
    await initdb()
    yield
    print("server is stopping")


app = FastAPI(
    title='Bookly',
    description='A RESTful API for a book review web service',
    version=version,
    lifespan=lifespan # add the lifespan event to our application
    
)

app.include_router(book_router,prefix=f"/api/{version}/books", tags=['books'])