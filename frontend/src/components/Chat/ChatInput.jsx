import { useState } from 'react';
import './ChatInput.css';

export default function ChatInput({ onSend, disabled }) {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim() && !disabled) {
      onSend(text.trim());
      setText('');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <form className="chat-input" onSubmit={handleSubmit}>
      <div className="chat-input__wrapper">
        <input
          type="text"
          className="chat-input__field"
          placeholder={disabled ? 'Thinking...' : 'Ask anything about campus...'}
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={disabled}
          id="chat-input-field"
          autoComplete="off"
        />
        <button
          type="submit"
          className="chat-input__send"
          disabled={disabled || !text.trim()}
          aria-label="Send message"
          id="chat-send-btn"
        >
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <line x1="22" y1="2" x2="11" y2="13" />
            <polygon points="22 2 15 22 11 13 2 9 22 2" />
          </svg>
        </button>
      </div>
      <p className="chat-input__hint">Powered by MCP Servers • Press Enter to send</p>
    </form>
  );
}
