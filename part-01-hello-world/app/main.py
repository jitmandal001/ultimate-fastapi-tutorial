from fastapi import FastAPI, APIRouter


app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()

@api_router.get("/hello", status_code=200)
def hello (x: int) -> dict:
    """
    Root GET
    """
    return {"msg": f"x = {x}"}

@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Welcome to the Recipe API!, i am Jit"}

@api_router.get("/items/{item_id}", status_code=200)
def get_item(item_id: int) -> dict:
    return {"item_id": item_id}

app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
