from typing import List

class RetrieverInterface:
    def __init__(self) -> None:
        pass

    def retrieve_top_k(self, query_embeddings: List[float], embeddings: List[List[float]], k: int):
        raise NotImplementedError("Subclass must implement this method")