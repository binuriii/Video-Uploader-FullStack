from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv() # look presense of .env & load them

imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),
    url_endpoint=os.getenv("IMAGEKIT_URL"),
)