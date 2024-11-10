# app.py

from fastapi import FastAPI, HTTPException
from transliteration_utils import process_text

app = FastAPI(
    title="Transliteration API",
    description="API for various transliteration conversions between different scripts.",
    version="1.0.0"
)
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

@app.get("/transliterate/", tags=["Transliteration"])
async def transliterate_endpoint(transliteration_type: str, text: str):
    """
    Transliterate text based on the specified transliteration type.
    
    - **transliteration_type**: The type of transliteration (e.g., `Gurmukhi2Shahmukhi`, `Shahmukhi2Gurmukhi`, `SindhiDEV2Roman`, `HindiToUrdu`)
    - **text**: The text to be transliterated
    """
    try:
        result = process_text(text, transliteration_type)
        return {"result": result}
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Individual endpoints for each transliteration type
@app.get("/transliterate/AutoDetectPersioArabicScript", tags=["Transliteration"])
async def autodetect_persio_arabic_script(text: str):
    return await transliterate_endpoint("AutoDetectPersioArabicScript", text)

@app.get("/transliterate/AutoDetectSindhiHindiScript", tags=["Transliteration"])
async def autodetect_sindhi_hindi_script(text: str):
    return await transliterate_endpoint("AutoDetectSindhiHindiScript", text)

@app.get("/transliterate/GurmukhiToShahmukhi", tags=["Transliteration"])
async def gurmukhi_to_shahmukhi(text: str):
    return await transliterate_endpoint("Gurmukhi2Shahmukhi", text)

@app.get("/transliterate/HindiToUrdu", tags=["Transliteration"])
async def hindi_to_urdu(text: str):
    return await transliterate_endpoint("Hindi2Urdu", text)

@app.get("/transliterate/ShahmukhiToGurmukhi", tags=["Transliteration"])
async def shahmukhi_to_gurmukhi(text: str):
    return await transliterate_endpoint("Shahmukhi2Gurmukhi", text)

@app.get("/transliterate/SindhiDEVToRoman", tags=["Transliteration"])
async def sindhi_dev_to_roman(text: str):
    return await transliterate_endpoint("SindhiDEV2Roman", text)

@app.get("/transliterate/SindhiDEVToSindhiUR", tags=["Transliteration"])
async def sindhi_dev_to_sindhi_ur(text: str):
    return await transliterate_endpoint("SindhiDEV2SindhiUR", text)

@app.get("/transliterate/SindhiURToSindhiDEV", tags=["Transliteration"])
async def sindhi_ur_to_sindhi_dev(text: str):
    return await transliterate_endpoint("SindhiUR2SindhiDEV", text)

@app.get("/transliterate/UrduToHindi", tags=["Transliteration"])
async def urdu_to_hindi(text: str):
    return await transliterate_endpoint("Urdu2Hindi", text)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)