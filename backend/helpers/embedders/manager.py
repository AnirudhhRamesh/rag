from .bert_embedder import BertEmbedder

class EmbedderManager:
    def __init__(self, config: dict) -> None:
        self.embedder = self.get_embedder(config["EMBEDDER"])

    def embed(self, chunks: list[str]) -> list[float]:
        return self.embedder.embed(chunks)

    def get_embedder(self, embedder_name: str):
        embedders = {
            "bert": BertEmbedder()
        }

        if embedder_name not in embedders:
            raise ValueError(f"Embedder {embedder_name} not found")

        return embedders[embedder_name]