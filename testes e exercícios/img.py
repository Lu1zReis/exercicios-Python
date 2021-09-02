from PIL import Image
import requests
from StringIO import StringIO

response = requests.get(url)
img = Image.open(StringIO(response.content))