import openai
from config.config import CHAT_GPT_API_KEY

openai.api_key = CHAT_GPT_API_KEY

def generate_image(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        print(f"Error generating image: {e}")
        return None
