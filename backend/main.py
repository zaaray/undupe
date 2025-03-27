from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend dev port
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/search/")
async def search_product(
    product_url: str = Form(None),
    image: UploadFile = None
):
    # Just return mock data for now
    return JSONResponse({
        "query": product_url or image.filename,
        "matches": [
            {"site": "Amazon", "title": "Wireless Earbuds Pro", "price": "$39.99", "url": "https://amazon.com/xyz"},
            {"site": "AliExpress", "title": "Bluetooth Earbuds", "price": "$12.99", "url": "https://aliexpress.com/abc"},
            {"site": "Temu", "title": "TWS Earphones", "price": "$10.49", "url": "https://temu.com/def"},
        ]
    })
