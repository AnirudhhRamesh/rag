from .interface import ChunkerInterface

class SentenceChunker(ChunkerInterface):
    def __init__(self):
        pass

    def chunk(self, text):
        return text.split("\n")