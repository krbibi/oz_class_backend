from fastapi import FastAPI
from routes import route as book_route


app = FastAPI()
app.include_router(book_route, prefix='/api/v1/books')

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app",reload=True)