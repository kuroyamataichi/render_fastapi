from typing import Optional

from fastapi import FastAPI

import random

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

from fastapi.responses import HTMLResponse #インポート
from fastapi import FastAPI

### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Like HTML</title>
        </head>
        <body>
            <h1>好きな漫画を紹介</h1>
            <h1>タッチ</h1>
            <img src="https://i.daily.jp/gossip/2017/06/30/Images/f_10327652.jpg" alt="タッチの画像" width="400">
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)