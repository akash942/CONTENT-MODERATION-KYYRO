from typing import Union
from nudenet import NudeDetector
from fastapi import FastAPI, File, UploadFile

detector = NudeDetector()
 
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return {"message": "Hello from Koyeb"}

@app.post('/detect/')
async def detect(file: UploadFile):
    image = await file.read()
    detections = detector.detect(image)
    # print(detections)
    return {"detections": detections}
