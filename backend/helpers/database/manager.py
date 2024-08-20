from typing import List
from .interface import DatabaseInterface
from .simple_db import SimpleDatabase
from .vector_db import VectorDatabase

class DatabaseManager:
    def __init__(self, config):
        self.config = config
        self.selected_db = self.get_database(config["DATABASE_TYPE"])

    def store_embeddings(self, embeddings: List[float]):
        return self.selected_db.store_embeddings(embeddings)

    def get_embeddings(self) -> List[float]:
        return self.selected_db.get_embeddings()

    def get_database(self, database_type: str) -> DatabaseInterface:
        databases = {
            "simple": SimpleDatabase(),
            "vector": VectorDatabase()
        }

        if database_type not in databases:
            raise ValueError(f"Database type {database_type} not supported")
        
        return databases[database_type]