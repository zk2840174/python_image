from typing import Union

from fastapi import FastAPI, HTTPException

import test3
from test3 import searchImages

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}







@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/searchImage")
async def searchImageGET(fileStr: Union[str, None] = None):

    if fileStr is None:
        raise HTTPException(status_code=400, detail="Query parameter 'fileStr' is required.")

    print("fileName")
    print(fileStr)

    try:
        results = searchImages("D:\\zzz\\food", "C:\\zzz\\"+ fileStr)
        print(results)
    except Exception as e:
        print(f"Error occurred while searching images: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


    print(results)


    return results['ids'][0]
