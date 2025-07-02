import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const result = await axios.post('http://localhost:8000/query', {
        text: query,
      });
      setResponse(result.data);
    } catch (error) {
      console.error('Error:', error);
      setResponse({ error: 'Failed to get response' });
    }

    setLoading(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>MOSDAC Help Bot</h1>
      </header>
      
      <main>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Ask your question..."
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Processing...' : 'Submit'}
          </button>
        </form>

        {response && (
          <div className="response">
            <p><strong>Answer:</strong> {response.answer}</p>
            <p><strong>Confidence:</strong> {response.confidence}</p>
            <div>
              <strong>Sources:</strong>
              <ul>
                {response.sources.map((source, index) => (
                  <li key={index}>{source}</li>
                ))}
              </ul>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;