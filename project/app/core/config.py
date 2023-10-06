from dotenv import load_dotenv
import os

load_dotenv()

api_url: str = f"/api/{os.getenv('VERSION','v1')}"
