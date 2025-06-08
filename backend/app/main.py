from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

TOPICS = {
    "sumatorias": "summation",
    "algebra": "algebra",
    "geometria": "geometry",
}

def generate_sumatorias():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    correct = a + b
    options = [correct,
               correct + random.randint(1, 5),
               correct - random.randint(1, 5)]
    random.shuffle(options)
    return {
        "question": f"¿Cuánto es {a} + {b}?",
        "options": options,
        "answer": correct,
    }

# Additional topic generator examples
def generate_algebra():
    a = random.randint(2, 10)
    b = random.randint(1, 9)
    correct = a * b
    options = [correct,
               correct + random.randint(1, 5),
               abs(correct - random.randint(1, 5))]
    random.shuffle(options)
    return {
        "question": f"¿Cuánto es {a}x cuando x={b}?",
        "options": options,
        "answer": correct,
    }

GENERATORS = {
    "sumatorias": generate_sumatorias,
    "algebra": generate_algebra,
}

@app.get("/generate/{topic}")
def generate_question(topic: str, timer: int = 30):
    if topic not in GENERATORS:
        raise HTTPException(status_code=404, detail="Tema no encontrado")
    q = GENERATORS[topic]()
    q["timer"] = timer
    return q
