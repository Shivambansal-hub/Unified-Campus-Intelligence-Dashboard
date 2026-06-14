import './TopBar.css';

export default function TopBar({ onToggleChat, isChatOpen }) {
  const now = new Date();
  const greeting = now.getHours() < 12 ? 'Good Morning' : now.getHours() < 17 ? 'Good Afternoon' : 'Good Evening';
  const dateStr = now.toLocaleDateString('en-IN', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });

  return (
    <header className="topbar">
      <div className="topbar__left">
        <div>
          <h2 className="topbar__greeting">{greeting}, Student! 👋</h2>
          <p className="topbar__date">{dateStr}</p>
        </div>
      </div>

      <div className="topbar__right">
        <button
          className={`topbar__chat-toggle ${isChatOpen ? 'topbar__chat-toggle--active' : ''}`}
          onClick={onToggleChat}
          aria-label="Toggle AI chat"
          id="toggle-chat-btn"
        >
          <span className="topbar__chat-icon">🤖</span>
          <span className="topbar__chat-label">AI Assistant</span>
          {!isChatOpen && <span className="topbar__chat-badge">Ask me!</span>}
        </button>

        <div className="topbar__avatar" id="user-avatar">
          <span>S</span>
        </div>
      </div>
    </header>
  );
}
