from typing import List

from .interface import RerankerInterface

class SimpleReranker(RerankerInterface):
    def __init__(self) -> None:
        super().__init__()

    def rerank(self, query: str, chunks: List[str]) -> List[str]:
        return chunks