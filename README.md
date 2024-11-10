# Transliteration API

## Overview

The Transliteration API is a FastAPI-based application that provides endpoints for various script transliterations. This API enables users to transliterate text between different scripts and languages, including Persian-Arabic, Sindhi-Hindi, Gurmukhi-Shahmukhi, and more, using an external service for processing.

![Transliteration API](/screencapture.png)

## Features

- **Dynamic Transliteration**: Supports multiple script conversions, allowing seamless text transliterations between languages.
- **RESTful API**: Provides well-defined REST endpoints with automatic OpenAPI documentation.
- **Modular Design**: Each transliteration type is managed with dedicated functions to enable easy updates and maintenance.
- **External API Integration**: Uses an external API for transliteration processing, ensuring high accuracy for complex scripts.

## API Endpoints

### Root

- **`GET /`** - Displays available transliteration routes.

### Transliteration Endpoints

- **`POST /transliterate/AutoDetectPersioArabicScript`** - Auto-detects Persian-Arabic script and transliterates accordingly.
- **`POST /transliterate/AutoDetectSindhiHindiScript`** - Auto-detects Sindhi-Hindi script and transliterates accordingly.
- **`POST /transliterate/GurmukhiToShahmukhi`** - Converts Gurmukhi script to Shahmukhi script.
- **`POST /transliterate/HindiToUrdu`** - Converts Hindi script to Urdu script.
- **`POST /transliterate/ShahmukhiToGurmukhi`** - Converts Shahmukhi script to Gurmukhi script.
- **`POST /transliterate/SindhiDEVToRoman`** - Converts SindhiDEV script to Roman script.
- **`POST /transliterate/SindhiDEVToSindhiUR`** - Converts SindhiDEV script to SindhiUR script.
- **`POST /transliterate/SindhiURToSindhiDEV`** - Converts SindhiUR script to SindhiDEV script.
- **`POST /transliterate/UrduToHindi`** - Converts Urdu script to Hindi script.

### Example JSON Output

Each endpoint returns a JSON response with the transliterated text:

```json
{
  "result": "میں ایک نرتکی ہوں"
}
```

### Installation
##### 1. Clone the Repository:

```bash
git clone https://github.com/Agamya-Samuel/Indicwiki-transliterate-api.git
cd Indicwiki-transliterate-api
```

##### 2. Install Dependencies:

```bash
pip install -r requirements.txt
```

##### 3. Run the Server:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
##### 4. Access API Documentation: 
Open your browser and go to http://127.0.0.1:8000/docs to view the auto-generated API documentation.

### Usage
Once the server is running, you can make requests to the API using a tool like curl or Postman.

### Example Request
Transliterate Text from Hindi to Urdu
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/transliterate/HindiToUrdu' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "नमस्ते"
}'
```

### Example JSON Response
```json
{
  "result": "ہیلو"
}
```

### Error Handling
- 404 Not Found: Returned when a specified transliteration type is not supported.
- 500 Internal Server Error: Returned for any server-side issues, including connectivity to the external API.

### License
This project is licensed under the MIT License.
<!-- See the LICENSE file for more information. -->