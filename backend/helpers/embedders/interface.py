class EmbedderInterface:
    def __init__(self):
        pass

    def embed(self, chunks: list[str]) -> list[float]:
        raise NotImplementedError("Subclass must implement this method")