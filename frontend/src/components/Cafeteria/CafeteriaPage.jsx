import { useState, useEffect } from 'react';
import { getTodayMenu, getSpecials } from '../../services/api';
import './CafeteriaPage.css';

const MEAL_TABS = [
  { key: 'breakfast', icon: '🌅', label: 'Breakfast' },
  { key: 'lunch', icon: '☀️', label: 'Lunch' },
  { key: 'dinner', icon: '🌙', label: 'Dinner' },
  { key: 'snacks', icon: '🍿', label: 'Snacks' },
];

export default function CafeteriaPage() {
  const [menu, setMenu] = useState(null);
  const [specials, setSpecials] = useState(null);
  const [activeMeal, setActiveMeal] = useState('lunch');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const [menuData, specialsData] = await Promise.all([getTodayMenu(), getSpecials()]);
        setMenu(menuData);
        setSpecials(specialsData);
        // Auto-select current meal
        const hour = new Date().getHours();
        if (hour < 10) setActiveMeal('breakfast');
        else if (hour < 15) setActiveMeal('lunch');
        else if (hour < 18) setActiveMeal('snacks');
        else setActiveMeal('dinner');
      } catch (e) {
        console.error('Cafeteria fetch error:', e);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  const currentMeal = menu?.meals?.[activeMeal];
  const mealItems = currentMeal?.items || [];
  const mealTiming = currentMeal?.timing || '';

  return (
    <div className="cafeteria-page">
      <div className="cafeteria-page__header animate-fade-in-up">
        <div>
          <h1 className="cafeteria-page__title">🍽️ Campus Cafeteria</h1>
          <p className="cafeteria-page__subtitle">
            {menu ? `${menu.day}'s Menu • ${menu.date}` : 'Loading menu...'}
          </p>
        </div>
      </div>

      {/* Today's Specials */}
      {specials?.specials?.length > 0 && (
        <div className="cafeteria-page__specials animate-fade-in-up stagger-1">
          <h2 className="cafeteria-page__specials-title">⭐ Today's Specials</h2>
          <div className="cafeteria-page__specials-grid">
            {specials.specials.map((s, i) => {
              const item = s.item;
              return (
                <div key={i} className="cafeteria-page__special-card glass-card">
                  <div className="cafeteria-page__special-badge">⭐ SPECIAL</div>
                  <h3>{item.name}</h3>
                  <p className="cafeteria-page__special-desc">{item.description}</p>
                  <div className="cafeteria-page__special-meta">
                    <span className={`badge ${item.is_veg ? 'badge-veg' : 'badge-nonveg'}`}>
                      {item.is_veg ? '🟢 Veg' : '🔴 Non-Veg'}
                    </span>
                    <span className="cafeteria-page__special-price">₹{item.price}</span>
                  </div>
                  <p className="cafeteria-page__special-timing">{s.meal_type} • {s.timing}</p>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Meal Tabs */}
      <div className="cafeteria-page__tabs animate-fade-in-up stagger-2">
        {MEAL_TABS.map((tab) => (
          <button
            key={tab.key}
            className={`cafeteria-page__tab ${activeMeal === tab.key ? 'cafeteria-page__tab--active' : ''}`}
            onClick={() => setActiveMeal(tab.key)}
          >
            <span className="cafeteria-page__tab-icon">{tab.icon}</span>
            <span className="cafeteria-page__tab-label">{tab.label}</span>
            {activeMeal === tab.key && mealTiming && (
              <span className="cafeteria-page__tab-time">{mealTiming}</span>
            )}
          </button>
        ))}
      </div>

      {/* Menu Items */}
      <div className="cafeteria-page__menu animate-fade-in-up stagger-3">
        {loading ? (
          Array.from({ length: 4 }).map((_, i) => (
            <div key={i} className="cafeteria-page__skeleton glass-card" />
          ))
        ) : mealItems.length > 0 ? (
          mealItems.map((item, i) => (
            <div
              key={item.id}
              className={`cafeteria-page__item glass-card animate-fade-in-up stagger-${(i % 6) + 1}`}
            >
              <div className={`cafeteria-page__item-indicator ${item.is_veg ? 'cafeteria-page__item-indicator--veg' : 'cafeteria-page__item-indicator--nonveg'}`} />
              <div className="cafeteria-page__item-info">
                <h3 className="cafeteria-page__item-name">
                  {item.name}
                  {item.is_special && <span className="cafeteria-page__item-star">⭐</span>}
                </h3>
                <p className="cafeteria-page__item-desc">{item.description}</p>
                <div className="cafeteria-page__item-tags">
                  <span className={`badge ${item.is_veg ? 'badge-veg' : 'badge-nonveg'}`}>
                    {item.is_veg ? 'Veg' : 'Non-Veg'}
                  </span>
                  <span className="cafeteria-page__item-cal">🔥 {item.calories} cal</span>
                  {item.allergens?.length > 0 && (
                    <span className="cafeteria-page__item-allergens" title={`Allergens: ${item.allergens.join(', ')}`}>
                      ⚠️ {item.allergens.join(', ')}
                    </span>
                  )}
                </div>
              </div>
              <div className="cafeteria-page__item-price">
                ₹{item.price}
              </div>
            </div>
          ))
        ) : (
          <div className="cafeteria-page__empty">
            <span className="cafeteria-page__empty-icon">🍽️</span>
            <p>No items available for this meal</p>
          </div>
        )}
      </div>
    </div>
  );
}
