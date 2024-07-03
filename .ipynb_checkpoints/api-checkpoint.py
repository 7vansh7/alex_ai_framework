from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
  """
  Root endpoint that returns a simple message.
  """
  return {"message": "Hello, world!"}


