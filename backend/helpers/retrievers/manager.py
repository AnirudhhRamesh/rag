from typing import List

class RetrieverManager:

    def __init__(self, config: dict):
        self.retriever = self.get_retriever(config["RETRIEVER"])

    def get_retriever(self, retriever_name: str):
        pass

    def retrieve_top_k(self, query_embeddings: List[float], embeddings: List[List[float]], k: int):
        return self.retriever.retrieve_top_k(query_embeddings, embeddings, k)