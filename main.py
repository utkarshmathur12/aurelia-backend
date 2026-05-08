from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google import genai

# =========================
# GEMINI CLIENT
# =========================

client = genai.Client(api_key="AIzaSyBy_afjxc4DnllDSeU9zlRRqDNtMs2nn3M")

# =========================
# FASTAPI APP
# =========================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# PRODUCTS API
# =========================

@app.get("/products")
def get_products():

    return [
        {
            "id": 1,
            "name": "Obsidian Black Suit",
            "price": "$299"
        },
        {
            "id": 2,
            "name": "Golden Silk Dress",
            "price": "$499"
        }
    ]

# =========================
# AI CHAT API
# =========================

@app.post("/chat")
def chat(data: dict):

    try:

        user_message = data["message"]

        prompt = f"{user_message}"

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return {
            "reply": response.text
        }

    except Exception as e:

        return {
            "error": str(e)
        }