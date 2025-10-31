
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

# ===== إعداد المسارات =====
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

# ===== إنشاء التطبيق =====
app = FastAPI(title="Automed")

# ===== ربط مجلدات الستاتيك والقوالب =====
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# ===== الصفحة الرئيسية =====
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ===== فحص الصحة =====
@app.get("/api/health")
async def health():
    return {"ok": True, "service": "Automed", "status": "healthy"}

# ===== سكربت تعريفي (اختياري) =====
SCRIPT_EN = [
    "Welcome to Automed - your AI-powered pharma partner.",
    "I'm your smart persona for suppliers and buyers.",
    "Ask me about stock, expiry dates, prices, and instant insured payments.",
    "Automed — Reinventing how medicine moves. Launching soon."
]

@app.get("/api/persona/intro")
async def persona_intro():
    return JSONResponse({"en": SCRIPT_EN})
