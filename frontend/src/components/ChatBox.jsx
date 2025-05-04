export default function ChatBox({ history }) {
    return (
      <div style={{ marginTop: '1rem' }}>
        {history.map((entry, index) => (
          <div key={index} style={{ marginBottom: '1rem' }}>
            <div><strong>You:</strong> {entry.user}</div>
            <div><strong>AI:</strong> {entry.ai}</div>
          </div>
        ))}
      </div>
    );
  }
  