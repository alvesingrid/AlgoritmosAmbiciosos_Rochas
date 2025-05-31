from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .logic import interval_scheduling
from .models import Event

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:5500",
    # Adicione outras origens conforme necessário
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite apenas as origens especificadas
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os headers
)

@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à API!"}

@app.post("/schedule")
def schedule(events: list[Event]):
    result = interval_scheduling(events)
    return result
