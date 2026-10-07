from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv
from pydantic import BaseModel, EmailStr, Field
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

class CustomerInquiry(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    message: str = Field(min_length=3, max_length=2000)

class CustomerInquiryResponse(BaseModel):
    success: bool
    response: str

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")
N8N_API_KEY = os.getenv("N8N_API_KEY")


# Routes are prefixed with /api so Vercel routes them to the Python
# function automatically (no vercel.json rewrites needed).
@app.post("/api/customer-inquiry")
def customer_inquiry(data: CustomerInquiry) -> CustomerInquiryResponse:

    if not N8N_WEBHOOK_URL:
        raise HTTPException(
            status_code=500,
            detail="Server is not configured: N8N_WEBHOOK_URL is missing."
        )

    try:
        response = requests.post(
            N8N_WEBHOOK_URL,
            headers={
                "Content-Type": "application/json",
                "x-api-key": N8N_API_KEY or ""
            },
            json=data.model_dump(),
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        raise HTTPException(
            status_code=504,
            detail="The support automation took too long to respond."
        )

    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Unable to connect to the support automation."
        )

    except ValueError:
        raise HTTPException(
            status_code=502,
            detail="Invalid response received from the support automation."
        )
