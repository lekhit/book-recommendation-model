from helper import rem
import uvicorn
from fastapi import FastAPI

app = FastAPI()



@app.get("/")
async def root(book_isbn:str):
	return {'result':rem(book_isbn)}
	
@app.get("recommend/")
async def root(book_id:int):
	return {'result':rem(book_id)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

