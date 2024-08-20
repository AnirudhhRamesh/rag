from typing import List

from anthropic import Anthropic

from .interface import GeneratorInterface

class ClaudeGenerator(GeneratorInterface):
    def __init__(self, config):
        self.client = Anthropic(api_key=config["ANTHROPIC_API_KEY"])

    def generate(self, prompt: str) -> str:
        return self.client.messages.create(
            model="claude-3-",
            messages=[{"role": "user", "content": prompt}]
        )["content"][0]["text"]