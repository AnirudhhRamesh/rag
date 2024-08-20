import fastapi
from main import RAG
import logging

logging.basicConfig(level=logging.INFO)

rag = RAG()
app = fastapi.FastAPI()

@app.post("/upload")
async def upload(file: str):
    rag.upload(file)
    logging.info(f"File uploaded: {file}")
    return {"message": f"File uploaded: {file}"}

@app.get("/get")
async def get(query: str):
    response = rag.get(query)
    logging.info(f"Query received: {query}")
    return {"message": f"Query received: {query}"}