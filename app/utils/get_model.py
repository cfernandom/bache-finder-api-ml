from tensorflow.keras.models import load_model
from app.core.config import settings
import os

def get_model():
    model_path = settings.MODEL_PATH
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    print(f"Loading model from {model_path}")
    try:
        model = load_model(model_path)
        print("Model loaded successfully")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise e