from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")
SECRET_KEY = os.getenv("SECRET_KEY")

from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    NEO4J_URI, 
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

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