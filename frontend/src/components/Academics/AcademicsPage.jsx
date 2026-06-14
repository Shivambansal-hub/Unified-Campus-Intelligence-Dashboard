import { useState, useEffect } from 'react';
import { getCourses, getDeadlines, getResources } from '../../services/api';
import './AcademicsPage.css';

const TABS = [
  { key: 'courses', icon: '📖', label: 'Courses' },
  { key: 'deadlines', icon: '⏰', label: 'Deadlines' },
  { key: 'resources', icon: '📄', label: 'Resources' },
];

const DEPARTMENTS = ['All', 'Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 'Mathematics', 'Physics', 'Humanities'];

export default function AcademicsPage() {
  const [activeTab, setActiveTab] = useState('courses');
  const [courses, setCourses] = useState([]);
  const [deadlines, setDeadlines] = useState([]);
  const [resources, setResources] = useState([]);
  const [activeDept, setActiveDept] = useState('All');
  const [expandedCourse, setExpandedCourse] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const [coursesData, deadlinesData, resourcesData] = await Promise.all([
          getCourses(),
          getDeadlines(),
          getResources(),
        ]);
        setCourses(coursesData);
        setDeadlines(deadlinesData);
        setResources(resourcesData);
      } catch (e) {
        console.error('Academics fetch error:', e);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, []);

  const filteredCourses = activeDept === 'All'
    ? courses
    : courses.filter((c) => c.department === activeDept);

  return (
    <div className="academics-page">
      <div className="academics-page__header animate-fade-in-up">
        <h1 className="academics-page__title">📖 Academics</h1>
        <p className="academics-page__subtitle">Courses, deadlines, and academic resources</p>
      </div>

      {/* Tabs */}
      <div className="academics-page__tabs animate-fade-in-up stagger-1">
        {TABS.map((tab) => (
          <button
            key={tab.key}
            className={`academics-page__tab ${activeTab === tab.key ? 'academics-page__tab--active' : ''}`}
            onClick={() => setActiveTab(tab.key)}
          >
            <span>{tab.icon}</span>
            <span>{tab.label}</span>
            {tab.key === 'deadlines' && deadlines.length > 0 && (
              <span className="academics-page__tab-count">{deadlines.length}</span>
            )}
          </button>
        ))}
      </div>

      {/* Courses Tab */}
      {activeTab === 'courses' && (
        <div className="animate-fade-in">
          <div className="academics-page__dept-filters">
            {DEPARTMENTS.map((dept) => (
              <button
                key={dept}
                className={`academics-page__dept-chip ${activeDept === dept ? 'academics-page__dept-chip--active' : ''}`}
                onClick={() => setActiveDept(dept)}
              >
                {dept}
              </button>
            ))}
          </div>

          <div className="academics-page__courses">
            {loading ? (
              Array.from({ length: 4 }).map((_, i) => (
                <div key={i} className="academics-page__skeleton glass-card" />
              ))
            ) : filteredCourses.length > 0 ? (
              filteredCourses.map((course, i) => (
                <div
                  key={course.id}
                  className={`academics-page__course glass-card animate-fade-in-up stagger-${(i % 6) + 1}`}
                >
                  <div
                    className="academics-page__course-main"
                    onClick={() => setExpandedCourse(expandedCourse === course.id ? null : course.id)}
                    role="button"
                    tabIndex={0}
                    style={{ cursor: 'pointer' }}
                  >
                    <div className="academics-page__course-code">{course.code}</div>
                    <div className="academics-page__course-info">
                      <h3 className="academics-page__course-name">{course.name}</h3>
                      <p className="academics-page__course-instructor">
                        👤 {course.instructor} • {course.credits} credits • Sem {course.semester}
                      </p>
                    </div>
                    <span className="badge badge-info">{course.department.split(' ')[0]}</span>
                    <span className="academics-page__course-expand">
                      {expandedCourse === course.id ? '▲' : '▼'}
                    </span>
                  </div>

                  {expandedCourse === course.id && (
                    <div className="academics-page__course-details animate-fade-in">
                      <p className="academics-page__course-desc">{course.description}</p>
                      {course.prerequisites?.length > 0 && (
                        <p className="academics-page__course-prereqs">
                          <strong>Prerequisites:</strong> {course.prerequisites.join(', ')}
                        </p>
                      )}
                      <div className="academics-page__course-schedule">
                        <h4>📅 Schedule:</h4>
                        {course.schedule.map((slot, j) => (
                          <div key={j} className="academics-page__schedule-slot">
                            <span className="academics-page__schedule-day">{slot.day}</span>
                            <span className="academics-page__schedule-time">{slot.time}</span>
                            <span className="academics-page__schedule-room">📍 {slot.room}</span>
                            {slot.type !== 'lecture' && (
                              <span className="badge badge-warning">{slot.type}</span>
                            )}
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              ))
            ) : (
              <div className="academics-page__empty">No courses found for this department</div>
            )}
          </div>
        </div>
      )}

      {/* Deadlines Tab */}
      {activeTab === 'deadlines' && (
        <div className="academics-page__deadlines animate-fade-in">
          {loading ? (
            Array.from({ length: 4 }).map((_, i) => (
              <div key={i} className="academics-page__skeleton glass-card" />
            ))
          ) : deadlines.length > 0 ? (
            deadlines.map((dl, i) => {
              const daysLeft = Math.ceil((new Date(dl.date) - new Date()) / (1000 * 60 * 60 * 24));
              const urgency = daysLeft <= 2 ? 'error' : daysLeft <= 5 ? 'warning' : daysLeft <= 10 ? 'info' : 'success';
              const typeEmoji = { assignment: '📝', exam: '📋', project: '🗂️', registration: '📌' }[dl.type] || '📌';

              return (
                <div key={dl.id} className={`academics-page__deadline glass-card animate-fade-in-up stagger-${(i % 6) + 1}`}>
                  <div className={`academics-page__deadline-countdown academics-page__deadline-countdown--${urgency}`}>
                    <span className="academics-page__deadline-days">{daysLeft}</span>
                    <span className="academics-page__deadline-days-label">days</span>
                  </div>
                  <div className="academics-page__deadline-info">
                    <div className="academics-page__deadline-top">
                      <span className={`badge badge-${urgency}`}>{typeEmoji} {dl.type}</span>
                      <span className="academics-page__deadline-code">{dl.course_code}</span>
                    </div>
                    <h3 className="academics-page__deadline-title">{dl.title}</h3>
                    <p className="academics-page__deadline-desc">{dl.description}</p>
                    <p className="academics-page__deadline-date">
                      📅 {new Date(dl.date).toLocaleDateString('en-IN', { weekday: 'long', day: 'numeric', month: 'long' })}
                    </p>
                  </div>
                </div>
              );
            })
          ) : (
            <div className="academics-page__empty">No upcoming deadlines 🎉</div>
          )}
        </div>
      )}

      {/* Resources Tab */}
      {activeTab === 'resources' && (
        <div className="academics-page__resources animate-fade-in">
          {loading ? (
            Array.from({ length: 4 }).map((_, i) => (
              <div key={i} className="academics-page__skeleton glass-card" />
            ))
          ) : (
            resources.map((res, i) => {
              const typeIcon = { handbook: '📕', document: '📄', link: '🔗', form: '📋' }[res.type] || '📎';
              return (
                <a
                  key={res.id}
                  href={res.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className={`academics-page__resource glass-card animate-fade-in-up stagger-${(i % 6) + 1}`}
                >
                  <span className="academics-page__resource-icon">{typeIcon}</span>
                  <div className="academics-page__resource-info">
                    <h3>{res.title}</h3>
                    <p>{res.description}</p>
                    <span className="academics-page__resource-dept">{res.department}</span>
                  </div>
                  <span className="academics-page__resource-arrow">→</span>
                </a>
              );
            })
          )}
        </div>
      )}
    </div>
  );
}
