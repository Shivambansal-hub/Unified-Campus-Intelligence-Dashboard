const API_BASE = import.meta.env.VITE_API_URL || '';

async function fetchAPI(endpoint, options = {}) {
  try {
    const response = await fetch(`${API_BASE}${endpoint}`, {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    });

    if (!response.ok) {
      throw new Error(`API Error: ${response.status} ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error(`Failed to fetch ${endpoint}:`, error);
    throw error;
  }
}

// ── Chat ──
export const sendChatMessage = (message) =>
  fetchAPI('/api/chat', {
    method: 'POST',
    body: JSON.stringify({ message }),
  });

// ── Library ──
export const getBooks = (query) =>
  fetchAPI(`/api/library/books${query ? `?q=${encodeURIComponent(query)}` : ''}`);

export const getAvailableBooks = () =>
  fetchAPI('/api/library/books/available');

export const getBook = (id) =>
  fetchAPI(`/api/library/books/${id}`);

export const getLibraryStats = () =>
  fetchAPI('/api/library/stats');

// ── Cafeteria ──
export const getTodayMenu = () =>
  fetchAPI('/api/cafeteria/menu/today');

export const getWeekMenu = () =>
  fetchAPI('/api/cafeteria/menu/week');

export const getMeal = (mealType) =>
  fetchAPI(`/api/cafeteria/menu/${mealType}`);

export const getSpecials = () =>
  fetchAPI('/api/cafeteria/specials');

// ── Events ──
export const getEvents = (params = {}) => {
  const query = new URLSearchParams(params).toString();
  return fetchAPI(`/api/events/events${query ? `?${query}` : ''}`);
};

export const getTodayEvents = () =>
  fetchAPI('/api/events/events/today');

export const getThisWeekEvents = () =>
  fetchAPI('/api/events/events/this-week');

export const getEvent = (id) =>
  fetchAPI(`/api/events/events/${id}`);

export const getClubs = () =>
  fetchAPI('/api/events/clubs');

// ── Academics ──
export const getCourses = (params = {}) => {
  const query = new URLSearchParams(params).toString();
  return fetchAPI(`/api/academics/courses${query ? `?${query}` : ''}`);
};

export const getCourse = (code) =>
  fetchAPI(`/api/academics/courses/${code}`);

export const getSchedule = (department) =>
  fetchAPI(`/api/academics/schedule/${department}`);

export const getDeadlines = () =>
  fetchAPI('/api/academics/deadlines');

export const getResources = () =>
  fetchAPI('/api/academics/resources');

// ── Health ──
export const getHealthAll = () =>
  fetchAPI('/api/health/all');
