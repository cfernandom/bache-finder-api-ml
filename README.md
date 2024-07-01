# Bache Finder API ML-Project

This project uses a pre-trained Keras model to predict images through a FastAPI endpoint.

## Prerequisites

need to have the following tools installed for h5py:

```
sudo apt-get install pkg-config
sudo apt-get install libhdf5-dev
```

## Setup

1. Create a virtual environment:
    ```sh
    python -m venv env
    ```

2. Activate the virtual environment:
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On Unix or MacOS:
        ```sh
        source env/bin/activate
        ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Copy the model file to the root directory of the project. Ensure the model file is named CNN_BF_PY.h5, or adjust the filename in accordance with your model as specified in the app/core/config.py file.

5. Run the FastAPI application:
    ```sh
    uvicorn app.main:app --reload
    ```

6. Go to `http://127.0.0.1:8000` to see the welcome message.

7. Use the `/predict/` endpoint to make predictions.

    example:
    ```sh
    curl --location 'http://localhost:8000/predict' \
    --form 'file=@"/path_to_img/1_2.jpg"'
    ```
    response:

    ```json
    {"prediction":[[0.13054095208644867,0.13108479976654053,0.14114101231098175,0.09955856949090958,0.11344218999147415,0.06351987272500992,0.03114495612680912,0.08905033767223358,0.03987095132470131,0.07407043874263763,0.08657591044902802]]}
    ```