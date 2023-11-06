from fastapi import FastAPI

app=FastAPI()
@app.get("/")
def User():
    return {"Mag":"Test the git commit"}
