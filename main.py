from fastapi import FastAPI, Request, Response, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from generate_answer import return_answer

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/answer")
async def process_question(question: str = Form(...)):
    answer = return_answer(question)
    return answer
