import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { getLibraryStats, getSpecials, getThisWeekEvents, getDeadlines } from '../../services/api';
import './DashboardHome.css';

export default function DashboardHome() {
  const navigate = useNavigate();
  const [stats, setStats] = useState(null);
  const [specials, setSpecials] = useState(null);
  const [events, setEvents] = useState(null);
  const [deadlines, setDeadlines] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchAll() {
      try {
        const [libStats, cafSpecials, weekEvents, acadDeadlines] = await Promise.allSettled([
          getLibraryStats(),
          getSpecials(),
          getThisWeekEvents(),
          getDeadlines(),
        ]);
        setStats(libStats.status === 'fulfilled' ? libStats.value : null);
        setSpecials(cafSpecials.status === 'fulfilled' ? cafSpecials.value : null);
        setEvents(weekEvents.status === 'fulfilled' ? weekEvents.value : null);
        setDeadlines(acadDeadlines.status === 'fulfilled' ? acadDeadlines.value : null);
      } catch (e) {
        console.error('Dashboard fetch error:', e);
      } finally {
        setLoading(false);
      }
    }
    fetchAll();
  }, []);

  const statCards = [
    {
      icon: '📚',
      label: 'Books Available',
      value: stats ? `${stats.available_books}/${stats.total_books}` : '—',
      color: 'hsl(250, 90%, 65%)',
      path: '/library',
    },
    {
      icon: '⭐',
      label: "Today's Specials",
      value: specials?.specials ? `${specials.specials.length} items` : '—',
      color: 'hsl(40, 95%, 60%)',
      path: '/cafeteria',
    },
    {
      icon: '📅',
      label: 'Events This Week',
      value: events ? `${events.length} events` : '—',
      color: 'hsl(170, 80%, 55%)',
      path: '/events',
    },
    {
      icon: '⏰',
      label: 'Next Deadline',
      value: deadlines && deadlines.length > 0
        ? new Date(deadlines[0].date).toLocaleDateString('en-IN', { day: 'numeric', month: 'short' })
        : '—',
      color: 'hsl(0, 80%, 60%)',
      path: '/academics',
    },
  ];

  return (
    <div className="dashboard">
      {/* Welcome Banner */}
      <div className="dashboard__banner animate-fade-in-up">
        <div className="dashboard__banner-content">
          <h1 className="dashboard__banner-title">
            Welcome to <span className="text-gradient">MARS</span>
          </h1>
          <p className="dashboard__banner-subtitle">
            Multi-Access Resource System — Your unified campus hub
          </p>
          <p className="dashboard__banner-desc">
            Search the library, check today's menu, find events, and track deadlines — all in one place.
            Try the AI assistant for instant answers!
          </p>
        </div>
        <div className="dashboard__banner-art">
          <div className="dashboard__orb dashboard__orb--1" />
          <div className="dashboard__orb dashboard__orb--2" />
          <div className="dashboard__orb dashboard__orb--3" />
        </div>
      </div>

      {/* Stat Cards */}
      <div className="dashboard__stats">
        {statCards.map((card, i) => (
          <button
            key={card.label}
            className={`dashboard__stat-card glass-card animate-fade-in-up stagger-${i + 1}`}
            onClick={() => navigate(card.path)}
            style={{ '--card-accent': card.color }}
          >
            <div className="dashboard__stat-icon">{card.icon}</div>
            <div className="dashboard__stat-info">
              <span className="dashboard__stat-value">{loading ? '...' : card.value}</span>
              <span className="dashboard__stat-label">{card.label}</span>
            </div>
            <div className="dashboard__stat-glow" />
          </button>
        ))}
      </div>

      {/* Quick Info Grid */}
      <div className="dashboard__grid">
        {/* Upcoming Events */}
        <div className="dashboard__section glass-card animate-fade-in-up stagger-3">
          <div className="dashboard__section-header">
            <h2>📅 Upcoming Events</h2>
            <button className="btn btn-ghost" onClick={() => navigate('/events')}>View all →</button>
          </div>
          <div className="dashboard__section-content">
            {loading ? (
              <div className="dashboard__skeleton-list">
                {[1, 2, 3].map((i) => <div key={i} className="dashboard__skeleton-item" />)}
              </div>
            ) : events && events.length > 0 ? (
              events.slice(0, 4).map((evt) => (
                <div key={evt.id} className="dashboard__event-item">
                  <div className="dashboard__event-date">
                    <span className="dashboard__event-day">
                      {new Date(evt.date).toLocaleDateString('en-IN', { day: 'numeric' })}
                    </span>
                    <span className="dashboard__event-month">
                      {new Date(evt.date).toLocaleDateString('en-IN', { month: 'short' })}
                    </span>
                  </div>
                  <div className="dashboard__event-info">
                    <h4>{evt.title}</h4>
                    <p>{evt.club} • {evt.venue}</p>
                  </div>
                  <span className={`badge badge-${evt.category === 'tech' ? 'info' : evt.category === 'cultural' ? 'warning' : evt.category === 'sports' ? 'success' : 'error'}`}>
                    {evt.category}
                  </span>
                </div>
              ))
            ) : (
              <p className="dashboard__empty">No events this week</p>
            )}
          </div>
        </div>

        {/* Upcoming Deadlines */}
        <div className="dashboard__section glass-card animate-fade-in-up stagger-4">
          <div className="dashboard__section-header">
            <h2>⏰ Deadlines</h2>
            <button className="btn btn-ghost" onClick={() => navigate('/academics')}>View all →</button>
          </div>
          <div className="dashboard__section-content">
            {loading ? (
              <div className="dashboard__skeleton-list">
                {[1, 2, 3].map((i) => <div key={i} className="dashboard__skeleton-item" />)}
              </div>
            ) : deadlines && deadlines.length > 0 ? (
              deadlines.slice(0, 4).map((dl) => {
                const daysLeft = Math.ceil((new Date(dl.date) - new Date()) / (1000 * 60 * 60 * 24));
                const urgency = daysLeft <= 2 ? 'error' : daysLeft <= 5 ? 'warning' : 'success';
                return (
                  <div key={dl.id} className="dashboard__deadline-item">
                    <div className={`dashboard__deadline-urgency dashboard__deadline-urgency--${urgency}`}>
                      {daysLeft}d
                    </div>
                    <div className="dashboard__deadline-info">
                      <h4>{dl.title}</h4>
                      <p>{dl.course_code} • {new Date(dl.date).toLocaleDateString('en-IN', { day: 'numeric', month: 'short' })}</p>
                    </div>
                    <span className={`badge badge-${dl.type === 'exam' ? 'error' : dl.type === 'project' ? 'warning' : 'info'}`}>
                      {dl.type}
                    </span>
                  </div>
                );
              })
            ) : (
              <p className="dashboard__empty">No upcoming deadlines</p>
            )}
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="dashboard__actions animate-fade-in-up stagger-5">
        <h2 className="dashboard__actions-title">⚡ Quick Actions</h2>
        <div className="dashboard__actions-grid">
          {[
            { icon: '🔍', label: 'Search Books', path: '/library' },
            { icon: '🍽️', label: "Today's Menu", path: '/cafeteria' },
            { icon: '📋', label: 'My Schedule', path: '/academics' },
            { icon: '🏆', label: 'Sports Events', path: '/events' },
            { icon: '📝', label: 'Assignments Due', path: '/academics' },
            { icon: '🎭', label: 'Cultural Events', path: '/events' },
          ].map((action) => (
            <button
              key={action.label}
              className="dashboard__action-btn glass-card"
              onClick={() => navigate(action.path)}
            >
              <span className="dashboard__action-icon">{action.icon}</span>
              <span className="dashboard__action-label">{action.label}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
