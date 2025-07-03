from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import requests
import json

app = FastAPI()

class Query(BaseModel):
    text: str
    location: Optional[dict] = None

class Response(BaseModel):
    answer: str
    confidence: float
    sources: List[str]

@app.post("/query", response_model=Response)
async def process_query(query: Query):
    try:
        # Send query to Rasa
        rasa_response = requests.post(
            "http://rasa:5005/model/parse",
            json={"text": query.text}
        )
        rasa_data = rasa_response.json()

        # Process the response
        intent = rasa_data.get('intent', {}).get('name', '')
        confidence = rasa_data.get('intent', {}).get('confidence', 0)

        # Get answer from knowledge graph if neededdd
        if query.location:
            # Add geospatial processing here
            pass

        return Response(
            answer="Processed response based on intent: " + intent,
            confidence=confidence,
            sources=["knowledge_graph", "rasa"]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))