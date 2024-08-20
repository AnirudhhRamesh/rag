class ChunkerInterface:
    def __init__(self):
        pass

    def chunk(self, text):
        raise NotImplementedError("Subclass must implement this method")