import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import rehypeKatex from 'rehype-katex'
import 'katex/dist/katex.min.css'

export default function ChatBox({ history }) {
  return (
    <div style={{ marginTop: '1rem' }}>
      {history.map((entry, index) => (
        <div key={index} style={{ marginBottom: '1.5rem' }}>
          <div><strong>You:</strong> {entry.user}</div>
          <div><strong>AI:</strong></div>
          <div
            style={{
              backgroundColor: '#f0f0f0', // light gray
              color: '#000',              // black text
              padding: '1rem',
              borderRadius: '8px',
              fontFamily: 'sans-serif'
            }}
          >
            <ReactMarkdown
              children={entry.ai}
              remarkPlugins={[remarkGfm]}
              rehypePlugins={[rehypeKatex]}
            />
          </div>
        </div>
      ))}
    </div>
  );
}
