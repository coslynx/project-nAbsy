import requests
import os

class APIRequest:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_image_from_api(self, query):
        headers = {
            'Authorization': f'Client-ID {self.api_key}'
        }
        params = {
            'query': query,
            'per_page': 1
        }
        response = requests.get('https://api.unsplash.com/photos/random', headers=headers, params=params)
        
        if response.status_code == 200:
            image_url = response.json()[0]['urls']['regular']
            return image_url
        else:
            return None

    def download_image(self, image_url, save_path):
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            return True
        else:
            return False

    def send_image_to_discord(self, image_path):
        files = {
            'file': open(image_path, 'rb')
        }
        payload = {
            'content': 'Generated Image:'
        }
        response = requests.post('https://discord.com/api/webhooks/your_webhook_here', data=payload, files=files)
        
        if response.status_code == 200:
            return True
        else:
            return False