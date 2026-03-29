from fastapi import FastAPI

app = FastAPI(title="Calculator API")

@app.post("/add")
async def add(a: float, b: float):
    return a+b


@app.post("/sum")
async def sum_numbers(a: float, b: float):
    return a-b


@app.post("/multiply")
async def multiply(a: float, b: float):
    return a*b
