import React, { useState } from 'react';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMessage = { sender: 'user', text: input };
    setMessages((msgs) => [...msgs, userMessage]);

    // Call your backend API to get bot response
    try {
      const response = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input }),
      });
      const data = await response.json();
      const botMessage = { sender: 'bot', text: data.reply };
      setMessages((msgs) => [...msgs, botMessage]);
    } catch (error) {
      const errorMessage = { sender: 'bot', text: 'Error: Could not reach server.' };
      setMessages((msgs) => [...msgs, errorMessage]);
    }

    setInput('');
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: '20px auto', fontFamily: 'Arial, sans-serif' }}>
      <h2>Chatbot Interface</h2>
      <div style={{ border: '1px solid #ccc', padding: 10, height: 400, overflowY: 'scroll' }}>
        {messages.map((msg, idx) => (
          <div key={idx} style={{ textAlign: msg.sender === 'user' ? 'right' : 'left', margin: '10px 0' }}>
            <span
              style={{
                display: 'inline-block',
                padding: '8px 12px',
                borderRadius: 15,
                backgroundColor: msg.sender === 'user' ? '#007bff' : '#e5e5ea',
                color: msg.sender === 'user' ? 'white' : 'black',
                maxWidth: '80%',
              }}
            >
              {msg.text}
            </span>
          </div>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={handleKeyPress}
        placeholder="Type your message..."
        style={{ width: '100%', padding: 10, marginTop: 10, boxSizing: 'border-box' }}
      />
      <button onClick={sendMessage} style={{ marginTop: 10, padding: '10px 20px' }}>
        Send
      </button>
    </div>
  );
}

export default App;