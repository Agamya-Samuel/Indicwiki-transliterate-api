# Transliteration API

## Overview

The Transliteration API is a FastAPI-based application that provides endpoints for various script transliterations. This API enables users to transliterate text between different scripts and languages, including Persian-Arabic, Sindhi-Hindi, Gurmukhi-Shahmukhi, and more, using an external service for processing.

## Features

- **Dynamic Transliteration**: Supports multiple script conversions, allowing seamless text transliterations between languages.
- **RESTful API**: Provides well-defined REST endpoints with automatic OpenAPI documentation.
- **Modular Design**: Each transliteration type is managed with dedicated functions to enable easy updates and maintenance.
- **External API Integration**: Uses an external API for transliteration processing, ensuring high accuracy for complex scripts.

## API Endpoints

### Root

- **`GET /`** - Displays available transliteration routes.

### Transliteration Endpoints

- **`GET /transliterate/AutoDetectPersioArabicScript`** - Auto-detects Persian-Arabic script and transliterates accordingly.
- **`GET /transliterate/AutoDetectSindhiHindiScript`** - Auto-detects Sindhi-Hindi script and transliterates accordingly.
- **`GET /transliterate/GurmukhiToShahmukhi`** - Converts Gurmukhi script to Shahmukhi script.
- **`GET /transliterate/HindiToUrdu`** - Converts Hindi script to Urdu script.
- **`GET /transliterate/ShahmukhiToGurmukhi`** - Converts Shahmukhi script to Gurmukhi script.
- **`GET /transliterate/SindhiDEVToRoman`** - Converts SindhiDEV script to Roman script.
- **`GET /transliterate/SindhiDEVToSindhiUR`** - Converts SindhiDEV script to SindhiUR script.
- **`GET /transliterate/SindhiURToSindhiDEV`** - Converts SindhiUR script to SindhiDEV script.
- **`GET /transliterate/UrduToHindi`** - Converts Urdu script to Hindi script.

## Code Explanation

### Main Components

1. **Root Route (`GET /`)**: Lists all available transliteration routes.
2. **Transliteration Endpoint** (`GET /transliterate/{transliteration_type}`): A generic route for handling various transliteration requests. This route takes in the transliteration type and the text to be processed.
3. **External API Request** (`process_text()`): Sends the text to an external transliteration API, specified by the `service` parameter, and processes the response.

### Functions

- **`process_text(text: str, service: str) -> str`**: Sends a request to the external API with the specified service type and processes the response, handling any necessary JSON decoding.
- **`transliterate_endpoint(transliteration_type: str, text: str)`**: Receives transliteration requests, validates the type, and uses `process_text()` to handle processing.

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
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
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
curl -X 'GET' \
  'http://127.0.0.1:8000/transliterate/HindiToUrdu?text=नमस्ते' \
  -H 'accept: application/json'
```

### Example JSON Response
```json
{
  "result": "السلام علیکم"
}
```

### Error Handling
- 404 Not Found: Returned when a specified transliteration type is not supported.
- 500 Internal Server Error: Returned for any server-side issues, including connectivity to the external API.

### License
This project is licensed under the MIT License.
<!-- See the LICENSE file for more information. -->