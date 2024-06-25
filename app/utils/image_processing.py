from PIL import Image
import numpy as np
from io import BytesIO

def process_image(image_bytes):
    image = Image.open(BytesIO(image_bytes)).convert("RGB") 
    image = image.resize((100, 100))
    image = np.array(image) / 255.0 # normalization
    image = np.expand_dims(image, axis=0) # add batch dimension
    return image