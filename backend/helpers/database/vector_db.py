from typing import List
from .interface import DatabaseInterface

class VectorDatabase(DatabaseInterface):
    def __init__(self, config):
        self.config = config

    def store_embeddings(self, embeddings: List[float]) -> None:
        raise NotImplementedError("Subclass must implement this method")

    def get_embeddings(self) -> List[float]:
        # TODO: Return every single embedding and then compute the distance?
        # Probably a vector DB would be optimized for searching closest neighbours data access pattern
        raise NotImplementedError("Subclass must implement this method")