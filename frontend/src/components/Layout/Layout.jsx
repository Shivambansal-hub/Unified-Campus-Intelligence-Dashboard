import { useState } from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';
import TopBar from './TopBar';
import ChatPanel from '../Chat/ChatPanel';
import './Layout.css';

export default function Layout() {
  const [isChatOpen, setIsChatOpen] = useState(false);

  return (
    <div className="layout">
      <Sidebar />
      <div className="layout__main">
        <TopBar
          onToggleChat={() => setIsChatOpen(!isChatOpen)}
          isChatOpen={isChatOpen}
        />
        <div className="layout__content-wrapper">
          <main className="layout__content">
            <Outlet />
          </main>
          <ChatPanel isOpen={isChatOpen} onClose={() => setIsChatOpen(false)} />
        </div>
      </div>
    </div>
  );
}
