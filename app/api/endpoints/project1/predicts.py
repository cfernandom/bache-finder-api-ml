from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from app.utils.image_processing import process_image
from app.models.project1_predict_models import predictModels

router = APIRouter()

@router.post("/")
async def predicts(file: UploadFile = File(...)):
    try:
        if file.content_type != "image/jpeg":
            return JSONResponse(
                status_code=400, content={"message": "Only JPEG image files are allowed."}
            )
        
        image = await file.read()
        
        processed_image = process_image(image)
        prediction = predictModels.predicts(processed_image)
        
        return JSONResponse(status_code=200, content={"predictions": prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})