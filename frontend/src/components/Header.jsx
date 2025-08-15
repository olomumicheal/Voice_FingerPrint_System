import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/HeaderFooterStyles.css';

/**
 * Header component for the application.
 * @returns {JSX.Element} The Header component.
 */
const Header = () => {
  return (
    <header className="app-header">
      <nav className="nav-container">
        <Link to="/" className="site-title">Voice Auth</Link>
        <ul className="nav-links">
          <li><Link to="/login" className="nav-link">Login</Link></li>
          <li><Link to="/register" className="nav-link">Register</Link></li>
          <li><Link to="/about" className="nav-link">About</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
