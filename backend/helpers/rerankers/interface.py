from typing import List

class RerankerInterface:
    def __init__(self) -> None:
        pass
    
    def rerank(self, query: str, chunks: List[str]) -> List[str]:
        raise NotImplementedError("Subclass must implement this method")