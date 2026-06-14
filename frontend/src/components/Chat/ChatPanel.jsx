import { useState, useRef, useEffect } from 'react';
import ChatMessage from './ChatMessage';
import ChatInput from './ChatInput';
import { sendChatMessage } from '../../services/api';
import './ChatPanel.css';

const SUGGESTED_QUESTIONS = [
  "What's for lunch today?",
  "Any tech events this week?",
  "Are there books on machine learning?",
  "What are my upcoming deadlines?",
  "Show me today's specials",
  "What clubs can I join?",
];

export default function ChatPanel({ isOpen, onClose }) {
  const [messages, setMessages] = useState([
    {
      id: 'welcome',
      role: 'assistant',
      content: "Hey there! 👋 I'm your MARS AI Assistant. I can help you find information across campus — library books, cafeteria menus, events, and academics. Just ask me anything!",
      sources: [],
      timestamp: new Date(),
    },
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async (text) => {
    if (!text.trim() || isLoading) return;

    const userMsg = {
      id: `user-${Date.now()}`,
      role: 'user',
      content: text,
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMsg]);
    setIsLoading(true);

    try {
      const data = await sendChatMessage(text);
      const assistantMsg = {
        id: `assistant-${Date.now()}`,
        role: 'assistant',
        content: data.response,
        sources: data.sources || [],
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, assistantMsg]);
    } catch (error) {
      const errorMsg = {
        id: `error-${Date.now()}`,
        role: 'assistant',
        content: "Oops! I couldn't reach the server. Make sure the backend is running. 🔌",
        sources: [],
        timestamp: new Date(),
        isError: true,
      };
      setMessages((prev) => [...prev, errorMsg]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSuggestion = (question) => {
    handleSend(question);
  };

  return (
    <div className={`chat-panel ${isOpen ? 'chat-panel--open' : ''}`}>
      <div className="chat-panel__header">
        <div className="chat-panel__header-left">
          <span className="chat-panel__avatar">🤖</span>
          <div>
            <h3 className="chat-panel__title">MARS AI</h3>
            <span className="chat-panel__status">
              <span className="chat-panel__status-dot" />
              Online
            </span>
          </div>
        </div>
        <button className="chat-panel__close" onClick={onClose} aria-label="Close chat">
          ✕
        </button>
      </div>

      <div className="chat-panel__messages" id="chat-messages">
        {messages.map((msg) => (
          <ChatMessage key={msg.id} message={msg} />
        ))}

        {isLoading && (
          <div className="chat-panel__thinking">
            <div className="thinking-dots">
              <span className="thinking-dot" />
              <span className="thinking-dot" />
              <span className="thinking-dot" />
            </div>
            <span className="thinking-label">Querying MCP servers...</span>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {messages.length <= 1 && (
        <div className="chat-panel__suggestions">
          <p className="chat-panel__suggestions-label">Try asking:</p>
          <div className="chat-panel__suggestions-grid">
            {SUGGESTED_QUESTIONS.map((q, i) => (
              <button
                key={i}
                className="chat-panel__suggestion-chip"
                onClick={() => handleSuggestion(q)}
              >
                {q}
              </button>
            ))}
          </div>
        </div>
      )}

      <ChatInput onSend={handleSend} disabled={isLoading} />
    </div>
  );
}
