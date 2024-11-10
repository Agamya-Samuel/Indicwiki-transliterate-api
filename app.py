# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transliteration_utils import process_text

app = FastAPI(
    title="Transliteration API",
    description="API for various transliteration conversions between different scripts.",
    version="1.0.0"
)

class TransliterationRequest(BaseModel):
    text: str

@app.get("/", tags=["Root"])
async def root():
    """
    Get a list of available transliteration routes.
    """
    available_routes = [
        {"route": "/transliterate/AutoDetectPersioArabicScript", "description": "Auto-detect Persian-Arabic Script"},
        {"route": "/transliterate/AutoDetectSindhiHindiScript", "description": "Auto-detect Sindhi-Hindi Script"},
        {"route": "/transliterate/GurmukhiToShahmukhi", "description": "Gurmukhi to Shahmukhi"},
        {"route": "/transliterate/HindiToUrdu", "description": "Hindi to Urdu"},
        {"route": "/transliterate/ShahmukhiToGurmukhi", "description": "Shahmukhi to Gurmukhi"},
        {"route": "/transliterate/SindhiDEVToRoman", "description": "SindhiDEV to Roman"},
        {"route": "/transliterate/SindhiDEVToSindhiUR", "description": "SindhiDEV to SindhiUR"},
        {"route": "/transliterate/SindhiURToSindhiDEV", "description": "SindhiUR to SindhiDEV"},
        {"route": "/transliterate/UrduToHindi", "description": "Urdu to Hindi"},
    ]
    return {"available_routes": available_routes}

@app.post("/transliterate/", tags=["Transliteration"])
async def transliterate_endpoint(transliteration_type: str, request: TransliterationRequest):
    """
    Transliterate text based on the specified transliteration type.
    
    - **transliteration_type**: The type of transliteration (e.g., `Gurmukhi2Shahmukhi`, `Shahmukhi2Gurmukhi`, `SindhiDEV2Roman`, `HindiToUrdu`)
    - **text**: The text to be transliterated
    """
    try:
        result = process_text(request.text, transliteration_type)
        return {"result": result}
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Individual endpoints for each transliteration type
@app.post("/transliterate/AutoDetectPersioArabicScript", tags=["Transliteration"])
async def autodetect_persio_arabic_script(request: TransliterationRequest):
    return await transliterate_endpoint("AutoDetectPersioArabicScript", request)

@app.post("/transliterate/AutoDetectSindhiHindiScript", tags=["Transliteration"])
async def autodetect_sindhi_hindi_script(request: TransliterationRequest):
    return await transliterate_endpoint("AutoDetectSindhiHindiScript", request)

@app.post("/transliterate/GurmukhiToShahmukhi", tags=["Transliteration"])
async def gurmukhi_to_shahmukhi(request: TransliterationRequest):
    return await transliterate_endpoint("Gurmukhi2Shahmukhi", request)

@app.post("/transliterate/HindiToUrdu", tags=["Transliteration"])
async def hindi_to_urdu(request: TransliterationRequest):
    return await transliterate_endpoint("Hindi2Urdu", request)

@app.post("/transliterate/ShahmukhiToGurmukhi", tags=["Transliteration"])
async def shahmukhi_to_gurmukhi(request: TransliterationRequest):
    return await transliterate_endpoint("Shahmukhi2Gurmukhi", request)

@app.post("/transliterate/SindhiDEVToRoman", tags=["Transliteration"])
async def sindhi_dev_to_roman(request: TransliterationRequest):
    return await transliterate_endpoint("SindhiDEV2Roman", request)

@app.post("/transliterate/SindhiDEVToSindhiUR", tags=["Transliteration"])
async def sindhi_dev_to_sindhi_ur(request: TransliterationRequest):
    return await transliterate_endpoint("SindhiDEV2SindhiUR", request)

@app.post("/transliterate/SindhiURToSindhiDEV", tags=["Transliteration"])
async def sindhi_ur_to_sindhi_dev(request: TransliterationRequest):
    return await transliterate_endpoint("SindhiUR2SindhiDEV", request)

@app.post("/transliterate/UrduToHindi", tags=["Transliteration"])
async def urdu_to_hindi(request: TransliterationRequest):
    return await transliterate_endpoint("Urdu2Hindi", request)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)