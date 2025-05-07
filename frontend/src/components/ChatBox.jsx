import ReactMarkdown from 'react-markdown'
import remarkMath from 'remark-math'
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
              backgroundColor: '#f9f9f9',
              color: '#111',
              padding: '1rem',
              borderRadius: '8px',
              fontFamily: 'Georgia, serif',
              fontSize: '1rem',
              lineHeight: '1.6',
              whiteSpace: 'pre-wrap',
            }}
          >
            <ReactMarkdown
              children={entry.ai}
              remarkPlugins={[remarkMath]}         // ✅ this enables math parsing
              rehypePlugins={[rehypeKatex]}        // ✅ this renders LaTeX using KaTeX
            />
          </div>
        </div>
      ))}
    </div>
  );
}
