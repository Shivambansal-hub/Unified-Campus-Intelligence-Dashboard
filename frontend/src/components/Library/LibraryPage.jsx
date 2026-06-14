import { useState, useEffect } from 'react';
import { getBooks, getLibraryStats } from '../../services/api';
import './LibraryPage.css';

const CATEGORIES = ['All', 'Computer Science', 'Physics', 'Mathematics', 'Literature', 'Engineering'];

export default function LibraryPage() {
  const [books, setBooks] = useState([]);
  const [stats, setStats] = useState(null);
  const [search, setSearch] = useState('');
  const [activeCategory, setActiveCategory] = useState('All');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const [booksData, statsData] = await Promise.all([getBooks(), getLibraryStats()]);
        setBooks(booksData);
        setStats(statsData);
      } catch (e) {
        console.error('Library fetch error:', e);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  const filtered = books.filter((b) => {
    const matchesSearch =
      !search ||
      b.title.toLowerCase().includes(search.toLowerCase()) ||
      b.author.toLowerCase().includes(search.toLowerCase());
    const matchesCategory = activeCategory === 'All' || b.category === activeCategory;
    return matchesSearch && matchesCategory;
  });

  return (
    <div className="library-page">
      <div className="library-page__header animate-fade-in-up">
        <div>
          <h1 className="library-page__title">📚 Campus Library</h1>
          <p className="library-page__subtitle">Browse and search the book catalog</p>
        </div>
        {stats && (
          <div className="library-page__stats-bar">
            <div className="library-page__stat">
              <span className="library-page__stat-num">{stats.total_books}</span>
              <span className="library-page__stat-lbl">Total</span>
            </div>
            <div className="library-page__stat-divider" />
            <div className="library-page__stat">
              <span className="library-page__stat-num library-page__stat-num--green">{stats.available_books}</span>
              <span className="library-page__stat-lbl">Available</span>
            </div>
            <div className="library-page__stat-divider" />
            <div className="library-page__stat">
              <span className="library-page__stat-num library-page__stat-num--red">{stats.checked_out}</span>
              <span className="library-page__stat-lbl">Checked Out</span>
            </div>
          </div>
        )}
      </div>

      {/* Search & Filter */}
      <div className="library-page__controls animate-fade-in-up stagger-1">
        <div className="library-page__search-wrapper">
          <span className="library-page__search-icon">🔍</span>
          <input
            type="text"
            className="library-page__search input"
            placeholder="Search by title, author, or category..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            id="library-search"
          />
        </div>
        <div className="library-page__filters">
          {CATEGORIES.map((cat) => (
            <button
              key={cat}
              className={`library-page__filter-chip ${activeCategory === cat ? 'library-page__filter-chip--active' : ''}`}
              onClick={() => setActiveCategory(cat)}
            >
              {cat}
            </button>
          ))}
        </div>
      </div>

      {/* Book Grid */}
      <div className="library-page__grid">
        {loading ? (
          Array.from({ length: 8 }).map((_, i) => (
            <div key={i} className="library-page__skeleton glass-card" />
          ))
        ) : filtered.length > 0 ? (
          filtered.map((book, i) => (
            <div
              key={book.id}
              className={`library-page__book glass-card animate-fade-in-up stagger-${(i % 6) + 1}`}
            >
              <div
                className="library-page__book-cover"
                style={{ background: `linear-gradient(135deg, ${book.cover_color}, ${book.cover_color}88)` }}
              >
                <span className="library-page__book-cover-text">{book.title.slice(0, 2)}</span>
              </div>
              <div className="library-page__book-info">
                <h3 className="library-page__book-title">{book.title}</h3>
                <p className="library-page__book-author">{book.author}</p>
                <div className="library-page__book-meta">
                  <span className="badge badge-info">{book.category}</span>
                  <span className={`badge ${book.available ? 'badge-success' : 'badge-error'}`}>
                    {book.available ? `✓ Available (${book.available_copies})` : `✗ Due ${book.due_date || 'soon'}`}
                  </span>
                </div>
                <div className="library-page__book-bottom">
                  <span className="library-page__book-shelf">📍 {book.shelf_location}</span>
                  <span className="library-page__book-isbn">{book.isbn}</span>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="library-page__empty">
            <span className="library-page__empty-icon">📭</span>
            <p>No books found matching your search</p>
          </div>
        )}
      </div>
    </div>
  );
}
