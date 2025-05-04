import { useState } from 'react';
import ChatBox from '../components/ChatBox';

export default function ChatPage() {
  const [prompt, setPrompt] = useState('');
  const [mode, setMode] = useState('critical');
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!prompt.trim()) return;
    setLoading(true);

    try {
      const res = await fetch('http://localhost:8000/submit_prompt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, mode, user_id: 'student001' })
      });
      const data = await res.json();

      setHistory((prev) => [...prev, { user: prompt, ai: data.response }]);
      setPrompt('');
    } catch (err) {
      setHistory((prev) => [...prev, { user: prompt, ai: 'Error: ' + err.message }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your question..."
        rows={3}
        style={{ width: '100%', marginBottom: '0.5rem' }}
      />
      <select value={mode} onChange={(e) => setMode(e.target.value)}>
        <option value="affirmative">Affirmative</option>
        <option value="critical">Critical</option>
      </select>
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? 'Thinking...' : 'Submit'}
      </button>

      <ChatBox history={history} />
    </div>
  );
}
