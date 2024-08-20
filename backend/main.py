import os

from helpers.database.manager import DatabaseManager
from helpers.chunkers.manager import ChunkManager
from helpers.embedders.manager import EmbedderManager
from helpers.retrievers.manager import RetrieverManager
from helpers.rerankers.manager import RerankerManager
from helpers.generators.manager import GeneratorManager

config = {
    "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
    "ASSEMBLYAI_API_KEY": os.getenv("ASSEMBLYAI_API_KEY"),
}

class RAG:
    def __init__(self):
        # TODO: Set-up a database
        self.db = DatabaseManager(config)

        # Set-up the helpers here
        self.chunker = ChunkManager(config)
        self.embedder = EmbedderManager(config)
        self.retriever = RetrieverManager(config)
        self.reranker = RerankerManager(config)
        self.generator = GeneratorManager(config)
        
        pass

    def upload_file(self, file_bytes: bytes):
        # Parse the bytes into a string
        file_text = file_bytes.decode("utf-8")

        # Chunk the file into sentences
        chunks = self.chunker.chunk(file_text)

        # Embed the chunks
        embeddings = self.embedder.embed(chunks)

        # Store the embeddings in the database
        self.db.store_embeddings(embeddings)


    def query(self, query: str) -> str:
        # Embed the query
        query_embedding = self.embedder.embed(query)

        # Retrieve the embeddings from the database
        embeddings = self.db.get_embeddings()

        # Get the top k chunks
        k = 5
        top_k_chunks = self.retriever.get_top_k(query_embedding, embeddings, k)

        # Re-rank to get the most relevant chunks
        reranked_chunks = self.reranker.rerank(query, top_k_chunks)

        # Generate a response
        response = self.generator.generate(query, reranked_chunks)

        return response