from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def read_root(request: Request):
    df = pd.read_csv('app/ip_addresses.csv')
    # Here you can process the dataframe as needed
    return templates.TemplateResponse("html/index.html", {"request": request, "data": df.to_dict()})
