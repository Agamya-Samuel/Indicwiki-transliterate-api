# transliteration_utils.py

from http.client import HTTPException
import requests
import json

TRANSLATION_API = "https://sangam.learnpunjabi.org/SindhiTransliteration.asmx"

def process_text(text: str, service: str) -> str:
    """
    Makes a request to the external transliteration service with specified text and service type.
    
    Parameters:
    - text (str): The text to be transliterated.
    - service (str): The specific transliteration type as required by the external API.
    
    Returns:
    - str: The response text from the transliteration service.
    """
    api_endpoint = f"{TRANSLATION_API}/{service}"
    text_ip = {"input": text}

    headers = {
        "User-Agent": "Wikimedia Toolforge transliteration service",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json; charset=utf-8",
        "X-Requested-With": "XMLHttpRequest"
    }

    response = requests.post(api_endpoint, data=json.dumps(text_ip), headers=headers)
    
    if response.status_code == 200:
        outer_response = response.json()
        inner_response = outer_response['d']
        return inner_response
    else:
        print("error...")
        raise HTTPException(status_code=response.status_code, detail="Error with external transliteration service")
