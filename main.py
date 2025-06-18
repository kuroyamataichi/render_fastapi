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
            <h1>名探偵コナン</h1>
            <p1>５歳から好き</p1>
            <img src="https://th.bing.com/th/id/R.71852eedc68cbb16b9b2468c40fec86b?rik=JGCVbG6QIshwmg&riu=http%3a%2f%2fwww.conan-portal.com%2fimg%2fstory_photo02.jpg&ehk=qpwXGVDU1c6hUKLRVv1JySVpwp62a%2bTerf9qIU%2bINwc%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1" alt="コナンの画像" width="400">

            <h1>タッチ</h1>
            <img src="https://i.daily.jp/gossip/2017/06/30/Images/f_10327652.jpg" alt="タッチの画像" width="400">

            <h1>H2</h1>
            <img src="https://ogre.natalie.mu/media/news/comic/2018/0805/H2_illust.jpg?imwidth=750&imdensity=1" alt="H2の画像" width="400">

            <h1>タッチ</h1>
            <img src="https://ogre.natalie.mu/media/news/comic/2016/0504/MIX.jpg?imwidth=750&imdensity=1" alt="mixの画像" width="400">

            <h1>刃牙</h1>
            <img src="https://baki-30th.com/wp-content/themes/baki30/img/ogimage2.png" alt="刃牙の画像" width="400">
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)