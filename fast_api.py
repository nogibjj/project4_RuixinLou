from fastapi import FastAPI
import uvicorn
from gcpconn import topFour
#from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"Hi, this is Ruixin Lou"}


@app.get("/topfour")
async def topfour():
    """Print the top five ranking stackoverflow posts"""

    result = topFour()
    print(result)
    # return {result.to_json(orient='table')}
    return result.to_string()


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")