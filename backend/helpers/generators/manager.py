from typing import List

from .interface import GeneratorInterface
from .claude_generator import ClaudeGenerator
from .gpt35_generator import GPT35Generator

class GeneratorManager:
    def __init__(self, config):
        self.config = config
        self.generator = self.get_generator(self.config.generator)

    def generate(self, query: str, chunks: List[str]) -> str:
        prompt = f""" 
        You are given the following query: {query}
        Here is the most relevant context: {chunks[0]}
        Here are also some potentially relevant context: {chunks[1:]}

        Given the query and the context, generate a response to the query.
        """
    
        return self.generator.generate(prompt)

    def get_generator(self, generator: str) -> GeneratorInterface:
        generators = {
            "claude": ClaudeGenerator(self.config),
            "gpt-3.5": GPT35Generator(self.config),
        }
        if generator not in generators:
            raise ValueError(f"Generator {generator} not found")

        return generators[generator]