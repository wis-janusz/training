from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_index():
    return {'Hello wordl!': '2'}

@app.get('/dane/')
def read_data():
    return {'Hello wordl!': '3'}

