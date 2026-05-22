from fastapi import FastAPI

app = FastAPI(title="Itinerary Rag")

@app.get("/health")
def health_check():
    return {"status": "ok"} 