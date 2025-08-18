import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import '../styles/RegisterationStyles.css'
import VoiceRecorder from '../components/VoiceRecorder';

/**
 * Registration page component with guided instructions.
 * @returns {JSX.Element} The RegistrationPage component.
 */
const RegistrationPage = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [voiceData, setVoiceData] = useState(null);
  const [message, setMessage] = useState('');
  const [showVoiceRecorder, setShowVoiceRecorder] = useState(false);

  const handleDetailsSubmit = (e) => {
    e.preventDefault();
    if (username && email && password) {
      setMessage("User details captured. Now, please record your voice.");
      setShowVoiceRecorder(true);
    } else {
      setMessage("Please fill in all user details first.");
    }
  };

  const handleRegistrationComplete = (recordedVoiceData) => {
    setMessage("Voice data successfully captured. Submitting details...");
    
    // Corrected logic: Change the key from voice_data to voice_sample
    const registrationData = {
      username,
      email,
      password,
      voice_sample: recordedVoiceData,
    };
    
    // Now send the combined data to the backend
    fetch('https://voice-fingerprint-system.onrender.com/api/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(registrationData),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      setMessage("Successfully captured user details and voice authentication. Redirecting to login page...");
      setTimeout(() => {
        navigate('/login');
      }, 2000); // Redirect after 2 seconds
    })
    .catch((error) => {
      console.error('Error:', error);
      setMessage("Registration failed. Please try again.");
    });
  };

  return (
    <div className="registration-container">
      <div className="registration-box">
        <h2 className="registration-title">Create an Account</h2>
        <form onSubmit={handleDetailsSubmit}>
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
          <div className="input-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="input-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="submit-details-button">Submit Details</button>
        </form>
        
        {message && <p className="registration-message">{message}</p>}
        
        {showVoiceRecorder && (
          <div className="voice-section">
            <p className="voice-prompt">Record your voice to create your voiceprint:</p>
            <VoiceRecorder onRecordComplete={handleRegistrationComplete} buttonText="Record Voice" />
          </div>
        )}
        
        <p className="registration-link-text">
          Already have an account? <Link to="/login" className="link-style">Log in here</Link>
        </p>
      </div>
    </div>
  );
};

export default RegistrationPage;
