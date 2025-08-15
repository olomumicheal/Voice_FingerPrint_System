import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/DashboardStyles.css';

/**
 * Dashboard page component.
 * @returns {JSX.Element} The DashboardPage component.
 */
const DashboardPage = () => {
  return (
    <div className="dashboard-container">
      <div className="dashboard-card">
        <h2 className="dashboard-title">Welcome to Your Dashboard!</h2>
        <p className="dashboard-message">
          You have successfully logged in using your unique voice.
        </p>
        <Link to="/login" className="logout-button">
          Log Out
        </Link>
      </div>
    </div>
  );
};

export default DashboardPage;
