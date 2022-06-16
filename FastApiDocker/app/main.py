from fastapi import FastAPI
import api

app = FastAPI()
app.include_router(api.router)

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to Balasundar's Technical Blog"}