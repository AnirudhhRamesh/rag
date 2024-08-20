from .interface import EmbedderInterface
from transformers import BertModel, BertTokenizer
import torch

class BertEmbedder(EmbedderInterface):
    def __init__(self):
        self.model = BertModel.from_pretrained("bert-base-uncased")
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def embed(self, chunks: list[str]) -> list[float]:
        encoded_input = self.tokenizer(chunks, padding=True, truncation=True, return_tensors="pt")
        encoded_input = {k: v.to(self.device) for k, v in encoded_input.items()}
        
        with torch.no_grad():
            model_output = self.model(**encoded_input)
        
        # Use the [CLS] token embeddings as the sentence embeddings
        embeddings = model_output.last_hidden_state[:, 0, :].cpu().numpy()
        return embeddings.tolist()