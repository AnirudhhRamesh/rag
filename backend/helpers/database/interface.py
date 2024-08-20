class DatabaseInterface:
    def __init__(self, config):
        self.config = config

    def store_embeddings(self, embeddings):
        raise NotImplementedError("Subclass must implement this method")

    def get_embeddings(self):
        # TODO: Return every single embedding and then compute the distance?
        # Probably a vector DB would be optimized for searching closest neighbours data access pattern
        raise NotImplementedError("Subclass must implement this method")