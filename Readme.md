# BAH-Project

A full-stack project with Rasa chatbot, FastAPI backend, React frontend, and Neo4j knowledge graph.

---

## 🚀 Quick Start

### 1. **Clone the repository**

```sh
git clone https://github.com/yourusername/BAH-Project.git
cd BAH-Project
```

### 2. **Set up Python environment**

```sh
python3.9 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. **Install Node.js dependencies for the frontend**

```sh
cd src/frontend
npm install
cd ../../
```

### 4. **Start Neo4j**

- **Neo4j Desktop:** Open and start your database.
- **Or Homebrew:**
  ```sh
  brew install neo4j
  neo4j start
  ```
- **Or Docker:**
  ```sh
  docker run -d --name neo4j -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/password neo4j:5
  ```

### 5. **Train the Rasa model**

```sh
cd src/chatbot
rasa train
cd ../../
```

### 6. **Run all services (development)**

Open three terminals:

**Terminal 1: Rasa**

```sh
cd src/chatbot
rasa run --enable-api
```

**Terminal 2: FastAPI**

```sh
cd src/api
uvicorn main:app --reload
```

**Terminal 3: React frontend**

```sh
cd src/frontend
npm start
```

---

## 🐳 Docker (All-in-one)

If you prefer Docker:

```sh
docker buildx build --platform linux/amd64 -t bah-project .
docker-compose up
```

---

## 📂 Project Structure

```
BAH-Project/
│
├── src/
│   ├── api/         # FastAPI backend
│   ├── chatbot/     # Rasa chatbot
│   └── frontend/    # React frontend
│
├── data/            # Neo4j data (gitignored)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .gitignore
```

---

## 📝 Notes

- All build, cache, and environment files are gitignored for easy setup.
- Update Neo4j credentials in your backend if you change the default password.
- For production, build the React app (`npm run build`) and serve with a static server.

---

## 🤝 Contributing

Pull requests are welcome!

---

## 📄 License

[MIT](LICENSE)
