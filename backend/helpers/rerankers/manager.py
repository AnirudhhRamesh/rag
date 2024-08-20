from typing import List

from helpers.reranker.interface import RerankerInterface
from helpers.reranker.simple_reranker import SimpleReranker

class RerankerManager:
    def __init__(self, config):
        self.reranker = self.get_reranker(config["RERANKER"])

    def rerank(self, query:str, chunks:List[str]) -> List[str]:
        return self.reranker.rerank(query, chunks)

    def get_reranker(self, reranker:str) -> RerankerInterface:
        rerankers = {
            "reranker": SimpleReranker()
        }

        if reranker not in rerankers:
            raise ValueError(f"Reranker {reranker} not found")
        
        return rerankers[reranker]