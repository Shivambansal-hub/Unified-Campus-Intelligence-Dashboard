import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout/Layout';
import DashboardHome from './components/Dashboard/DashboardHome';
import LibraryPage from './components/Library/LibraryPage';
import CafeteriaPage from './components/Cafeteria/CafeteriaPage';
import EventsPage from './components/Events/EventsPage';
import AcademicsPage from './components/Academics/AcademicsPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<DashboardHome />} />
          <Route path="library" element={<LibraryPage />} />
          <Route path="cafeteria" element={<CafeteriaPage />} />
          <Route path="events" element={<EventsPage />} />
          <Route path="academics" element={<AcademicsPage />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
