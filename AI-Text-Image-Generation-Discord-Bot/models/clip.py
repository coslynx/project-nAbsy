import discord
from models.dalle import DALLE

class ClipModel:
    def __init__(self):
        self.dalle_model = DALLE()

    def generate_image(self, text_input):
        try:
            image = self.dalle_model.generate_image(text_input)
            return image
        except Exception as e:
            print(f"Error generating image: {e}")
            return None

    def process_text_input(self, text_input):
        # Add any text processing logic here if needed
        return text_input

    async def display_image(self, text_input, channel):
        processed_text = self.process_text_input(text_input)
        image = self.generate_image(processed_text)

        if image:
            await channel.send(file=discord.File(image, "generated_image.png"))
        else:
            await channel.send("Failed to generate image. Please try again.")

    async def handle_command(self, message, channel):
        if message.content.startswith('!generate_image'):
            text_input = message.content[len('!generate_image'):].strip()
            await self.display_image(text_input, channel)