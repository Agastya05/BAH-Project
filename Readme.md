# AI-based Help Bot Project

## Overview

This project is an AI-based Help Bot that integrates a chatbot powered by Rasa, a knowledge graph, and a frontend interface. It uses FastAPI for the backend API server and Neo4j as the graph database.

## Project Structure

```
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── scripts/
│   └── start-services.sh
├── src/
│   ├── api/
│   │   └── main.py
│   ├── chatbot/
│   │   └── config.yml
│   ├── frontend/
│   │   ├── package.json
│   │   └── src/
│   ├── knowledge_graph/
│   │   └── graph_processor.py
│   ├── nlp/
│   │   └── text_processor.py
│   └── scrapers/
│       └── mosdac_spider.py
└── tests/
```

## Prerequisites

- Docker and Docker Compose installed
- Python 3.8+

## Setup and Running

### 1. Start Docker Services

Run the following command to start all services (Rasa, API, Neo4j, Frontend):

```bash
docker-compose up -d
```

### 2. Verify Running Containers

Check that all containers are running:

```bash
docker ps
```

### 3. Initialize Knowledge Graph

Run the graph processor to initialize the knowledge graph:

```bash
python src/knowledge_graph/graph_processor.py
```

### 4. Train Rasa Model

If needed, train the Rasa chatbot model:

```bash
rasa train
```

### 5. Access Frontend

Open your browser and go to:

```
http://localhost:3000
```

### 6. Test Chatbot

Send a POST request to the API:

```bash
curl http://localhost:8000/query -X POST -H "Content-Type: application/json" -d '{"text": "Hello"}'
```

## Troubleshooting

- If API returns connection errors to Rasa, ensure Rasa container is running and accessible.
- Check logs for API and Rasa:

```bash
docker-compose logs api
```

```bash
docker-compose logs rasa
```

## Development

- Backend API code is in `src/api/`
- Frontend React app is in `src/frontend/`
- Knowledge graph logic is in `src/knowledge_graph/`
- NLP utilities are in `src/nlp/`

## .gitignore

The project includes a comprehensive `.gitignore` covering Python, Docker, Node, Neo4j, and IDE files.

---

Feel free to ask if you need help with specific parts of the project or further customization.
