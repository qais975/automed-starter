from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Automed")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/health")
async def health():
    return {"ok": True, "service": "Automed", "status": "healthy"}

SCRIPT_EN = [
    "Welcome to Automed — your AI-powered pharma partner.",
    "I’m your smart persona for suppliers and buyers.",
    "Ask me about stock, expiry dates, prices, and instant insured payments.",
    "Automed — Reinventing how medicine moves. Launching soon."
]
SCRIPT_AR = [
    "مرحبًا بكم في أوتومِد — شريككم الدوائي المدعوم بالذكاء الاصطناعي.",
    "أنا البيرسونا الذكية للمورّدين والمشترين.",
    "اسألوني عن المخزون وتواريخ الانتهاء والأسعار والمدفوعات المضمونة الفورية.",
    "أوتومِد — نعيد ابتكار حركة الدواء. إطلاقٌ قريبًا."
]

@app.get("/api/persona/intro")
async def persona_intro():
    return JSONResponse({"en": SCRIPT_EN, "ar": SCRIPT_AR})
