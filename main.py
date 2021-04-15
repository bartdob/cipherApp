from src.cryp import encrypt, decrypted
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {
        'request': request,
    })

@app.post('/')
def form_post(request: Request, message: str = Form(...), key: str = Form(...)):
    result = encrypt(message, key)
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result,
    'message': message,
    'key': key })

@app.get("/decrypted", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("decrypted.html", {
        'request': request,
    })

@app.post('/decrypted')
def form_post(request: Request, message: str = Form(...), key: str = Form(...)):
    result = decrypted(message, key)
    return templates.TemplateResponse('decrypted.html', context={'request': request, 'result': result,
    'message': message,
    'key': key })
