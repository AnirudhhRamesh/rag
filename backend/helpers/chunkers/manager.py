from .interface import ChunkerInterface
from .sentence_chunker import SentenceChunker

class ChunkManager:
    def __init__(self, config: dict) -> None:
        self.selected_chunker = self.get_chunker(config["CHUNKER"])

    def chunk(self, text: str) -> list[str]:
        return self.selected_chunker.chunk(text)

    def get_chunker(self, chunker_name: str) -> ChunkerInterface:
        chunkers = {
            "sentence": SentenceChunker()
        }

        if chunker_name not in chunkers:
            raise ValueError(f"Chunker {chunker_name} not found")

        return chunkers[chunker_name]
