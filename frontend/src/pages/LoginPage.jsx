import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import '../styles/LoginStyles.css';
import VoiceRecorder from '../components/VoiceRecorder';

/**
 * Login page component.
 * @returns {JSX.Element} The LoginPage component.
 */
const LoginPage = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');

  const handleLogin = (voiceData) => {
    console.log("Attempting to log in with voice data:", voiceData);
    
    // For this temporary login logic, we are sending the username to the backend
    fetch('https://voice-auth-backend.onrender.com/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username: username }),
    })
    .then(response => {
      if (response.ok) {
        alert('Login successful!');
        navigate('/dashboard'); 
      } else {
        alert('Login failed!');
      }
      return response.json();
    })
    .then(data => {
      console.log('Server response:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
      alert('Login failed!');
    });
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h2 className="login-title">Log In with Your Voice</h2>
        <div className="input-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
        </div>
        <VoiceRecorder onRecordComplete={handleLogin} buttonText="Log In" />
        <p className="login-link-text">
          Don't have an account? <Link to="/register" className="link-style">Register here</Link>
        </p>
      </div>
    </div>
  );
};

export default LoginPage;
