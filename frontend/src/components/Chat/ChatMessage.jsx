import './ChatMessage.css';

const SOURCE_LABELS = {
  library: { icon: '📚', label: 'Library', color: 'hsl(250, 90%, 65%)' },
  cafeteria: { icon: '🍽️', label: 'Cafeteria', color: 'hsl(40, 95%, 60%)' },
  events: { icon: '📅', label: 'Events', color: 'hsl(170, 80%, 55%)' },
  academics: { icon: '📖', label: 'Academics', color: 'hsl(0, 80%, 60%)' },
};

export default function ChatMessage({ message }) {
  const isUser = message.role === 'user';
  const time = new Date(message.timestamp).toLocaleTimeString('en-IN', {
    hour: '2-digit',
    minute: '2-digit',
  });

  // Simple markdown-like formatting: bold, line breaks
  const formatContent = (text) => {
    if (!text) return '';
    return text
      .split('\n')
      .map((line, i) => {
        // Bold text: **text**
        const formatted = line.replace(
          /\*\*(.*?)\*\*/g,
          '<strong>$1</strong>'
        );
        return `<span key="${i}">${formatted}</span>`;
      })
      .join('<br/>');
  };

  return (
    <div className={`chat-msg ${isUser ? 'chat-msg--user' : 'chat-msg--assistant'} ${message.isError ? 'chat-msg--error' : ''}`}>
      {!isUser && (
        <div className="chat-msg__avatar">🤖</div>
      )}
      <div className="chat-msg__bubble">
        <div
          className="chat-msg__content"
          dangerouslySetInnerHTML={{ __html: formatContent(message.content) }}
        />

        {message.sources && message.sources.length > 0 && (
          <div className="chat-msg__sources">
            {message.sources.map((src) => {
              const info = SOURCE_LABELS[src] || { icon: '🔗', label: src, color: '#888' };
              return (
                <span
                  key={src}
                  className="chat-msg__source-badge"
                  style={{ '--badge-color': info.color }}
                >
                  {info.icon} {info.label}
                </span>
              );
            })}
          </div>
        )}

        <span className="chat-msg__time">{time}</span>
      </div>
    </div>
  );
}
