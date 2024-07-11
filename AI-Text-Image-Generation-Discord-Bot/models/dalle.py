from typing import List

import torch
import torchvision
from transformers import DALLEForConditionalGeneration, DALLETokenizer

class DALLEImageGenerator:
    def __init__(self):
        self.model = DALLEForConditionalGeneration.from_pretrained('openai/clip-dalle')
        self.tokenizer = DALLETokenizer.from_pretrained('openai/clip-dalle')

    def generate_image_from_text(self, text: str) -> torch.Tensor:
        input_ids = self.tokenizer(text, return_tensors='pt').input_ids
        output = self.model.generate(input_ids)
        image = torchvision.transforms.functional.to_pil_image(output)
        return image

    def generate_images_from_texts(self, texts: List[str]) -> List[torch.Tensor]:
        images = []
        for text in texts:
            image = self.generate_image_from_text(text)
            images.append(image)
        return images

    def save_image(self, image: torch.Tensor, filename: str):
        image.save(filename)

    def display_image(self, image: torch.Tensor):
        image.show()