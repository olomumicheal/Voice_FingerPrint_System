import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './styles/Global.css';
import './styles/HeaderFooterStyles.css';

// Pages
import LoginPage from './pages/LoginPage';
import RegistrationPage from './pages/RegisterationPage';
import About from './pages/About';
import DashboardPage from './pages/Dashboard';

// Components
import Header from './components/Header';
import Footer from './components/Footer';

/**
 * Main application component. Sets up routing for different pages.
 * @returns {JSX.Element} The main App component.
 */
function App() {
  return (
    <Router>
      <div className="app-container">
        <Header />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<LoginPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/register" element={<RegistrationPage />} />
            <Route path="/about" element={<About />} />
            <Route path="/dashboard" element={<DashboardPage />} /> {/* <-- Add this route */}
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
