from typing import List

from .interface import RetrieverInterface

class CosineRetriever(RetrieverInterface):
    def __init__(self, embeddings: List[List[float]]) -> None:
        self.embeddings = embeddings

    def retrieve_top_k(self, query_embeddings: List[float], embeddings: List[List[float]], k: int):
        # TODO: Replace float with np.array so you can use dot product efficiently
        pass