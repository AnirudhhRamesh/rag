from typing import List

class GeneratorInterface:
    def __init__(self) -> None:
        pass

    def generate(self, prompt: str):
        raise NotImplementedError("Subclass must implement this method")