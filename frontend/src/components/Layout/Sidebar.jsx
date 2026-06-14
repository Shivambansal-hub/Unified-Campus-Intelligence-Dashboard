import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import './Sidebar.css';

const navItems = [
  { path: '/', icon: '🏠', label: 'Dashboard' },
  { path: '/library', icon: '📚', label: 'Library' },
  { path: '/cafeteria', icon: '🍽️', label: 'Cafeteria' },
  { path: '/events', icon: '📅', label: 'Events' },
  { path: '/academics', icon: '📖', label: 'Academics' },
];

export default function Sidebar() {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <aside className={`sidebar ${collapsed ? 'sidebar--collapsed' : ''}`}>
      <div className="sidebar__header">
        <div className="sidebar__logo">
          <span className="sidebar__logo-icon">🚀</span>
          {!collapsed && <span className="sidebar__logo-text">MARS</span>}
        </div>
        <button
          className="sidebar__toggle btn-ghost"
          onClick={() => setCollapsed(!collapsed)}
          aria-label={collapsed ? 'Expand sidebar' : 'Collapse sidebar'}
        >
          {collapsed ? '→' : '←'}
        </button>
      </div>

      <nav className="sidebar__nav">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            end={item.path === '/'}
            className={({ isActive }) =>
              `sidebar__link ${isActive ? 'sidebar__link--active' : ''}`
            }
          >
            <span className="sidebar__link-icon">{item.icon}</span>
            {!collapsed && <span className="sidebar__link-label">{item.label}</span>}
            {!collapsed && (
              <span className="sidebar__link-indicator" />
            )}
          </NavLink>
        ))}
      </nav>

      <div className="sidebar__footer">
        {!collapsed && (
          <div className="sidebar__status">
            <div className="sidebar__status-dot" />
            <span>All systems online</span>
          </div>
        )}
      </div>
    </aside>
  );
}
