import { useState, useEffect } from 'react';
import { getEvents, getClubs } from '../../services/api';
import './EventsPage.css';

const CATEGORY_FILTERS = [
  { key: 'all', icon: '📋', label: 'All Events' },
  { key: 'tech', icon: '💻', label: 'Tech' },
  { key: 'cultural', icon: '🎭', label: 'Cultural' },
  { key: 'sports', icon: '🏆', label: 'Sports' },
  { key: 'academic', icon: '🎓', label: 'Academic' },
  { key: 'social', icon: '🤝', label: 'Social' },
];

export default function EventsPage() {
  const [events, setEvents] = useState([]);
  const [clubs, setClubs] = useState([]);
  const [activeCategory, setActiveCategory] = useState('all');
  const [showClubs, setShowClubs] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const [eventsData, clubsData] = await Promise.all([getEvents(), getClubs()]);
        setEvents(eventsData);
        setClubs(clubsData);
      } catch (e) {
        console.error('Events fetch error:', e);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  const filtered = activeCategory === 'all'
    ? events
    : events.filter((e) => e.category === activeCategory);

  const getCategoryEmoji = (cat) => {
    const map = { tech: '💻', cultural: '🎭', sports: '🏆', academic: '🎓', social: '🤝' };
    return map[cat] || '📅';
  };

  return (
    <div className="events-page">
      <div className="events-page__header animate-fade-in-up">
        <div>
          <h1 className="events-page__title">📅 Campus Events</h1>
          <p className="events-page__subtitle">{events.length} upcoming events across campus</p>
        </div>
        <button
          className={`btn ${showClubs ? 'btn-primary' : 'btn-secondary'}`}
          onClick={() => setShowClubs(!showClubs)}
        >
          {showClubs ? '📅 Events' : '🏛️ View Clubs'}
        </button>
      </div>

      {showClubs ? (
        /* Clubs Grid */
        <div className="events-page__clubs animate-fade-in">
          <div className="events-page__clubs-grid">
            {clubs.map((club, i) => (
              <div key={club.id} className={`events-page__club glass-card animate-fade-in-up stagger-${(i % 6) + 1}`}>
                <div className="events-page__club-header">
                  <span className="events-page__club-emoji">{getCategoryEmoji(club.category)}</span>
                  <span className={`badge badge-${club.category === 'tech' ? 'info' : club.category === 'cultural' ? 'warning' : 'success'}`}>
                    {club.category}
                  </span>
                </div>
                <h3 className="events-page__club-name">{club.name}</h3>
                <p className="events-page__club-desc">{club.description}</p>
                <div className="events-page__club-footer">
                  <span>👥 {club.member_count} members</span>
                  <span>📧 {club.contact_email}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      ) : (
        <>
          {/* Category Filters */}
          <div className="events-page__filters animate-fade-in-up stagger-1">
            {CATEGORY_FILTERS.map((f) => (
              <button
                key={f.key}
                className={`events-page__filter ${activeCategory === f.key ? 'events-page__filter--active' : ''}`}
                onClick={() => setActiveCategory(f.key)}
              >
                <span>{f.icon}</span>
                <span>{f.label}</span>
              </button>
            ))}
          </div>

          {/* Events Timeline */}
          <div className="events-page__timeline">
            {loading ? (
              Array.from({ length: 4 }).map((_, i) => (
                <div key={i} className="events-page__skeleton glass-card" />
              ))
            ) : filtered.length > 0 ? (
              filtered.map((evt, i) => {
                const date = new Date(evt.date);
                const isPast = date < new Date();
                return (
                  <div
                    key={evt.id}
                    className={`events-page__event glass-card animate-fade-in-up stagger-${(i % 6) + 1} ${isPast ? 'events-page__event--past' : ''}`}
                  >
                    <div className="events-page__event-date-col">
                      <span className="events-page__event-day">
                        {date.toLocaleDateString('en-IN', { day: 'numeric' })}
                      </span>
                      <span className="events-page__event-month">
                        {date.toLocaleDateString('en-IN', { month: 'short' })}
                      </span>
                      <span className="events-page__event-dow">
                        {date.toLocaleDateString('en-IN', { weekday: 'short' })}
                      </span>
                    </div>

                    <div className="events-page__event-line" />

                    <div className="events-page__event-content">
                      <div className="events-page__event-top">
                        <span className={`badge badge-${evt.category === 'tech' ? 'info' : evt.category === 'cultural' ? 'warning' : evt.category === 'sports' ? 'success' : 'error'}`}>
                          {getCategoryEmoji(evt.category)} {evt.category}
                        </span>
                        {!evt.is_free && (
                          <span className="events-page__event-fee">₹{evt.fee}</span>
                        )}
                      </div>
                      <h3 className="events-page__event-title">{evt.title}</h3>
                      <p className="events-page__event-club">{evt.club}</p>
                      <p className="events-page__event-desc">{evt.description}</p>
                      <div className="events-page__event-meta">
                        <span>🕐 {evt.time}</span>
                        <span>📍 {evt.venue}</span>
                        {evt.max_participants && (
                          <span>👥 {evt.current_registrations}/{evt.max_participants}</span>
                        )}
                      </div>
                      {evt.registration_link && (
                        <a
                          href={evt.registration_link}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="events-page__event-register btn btn-primary"
                        >
                          Register →
                        </a>
                      )}
                    </div>
                  </div>
                );
              })
            ) : (
              <div className="events-page__empty">
                <span>📭</span>
                <p>No events in this category</p>
              </div>
            )}
          </div>
        </>
      )}
    </div>
  );
}
