import React from 'react';
import '../styles/AboutStyles.css';

/**
 * About page component.
 * @returns {JSX.Element} The About component.
 */
const About = () => {
  return (
    <div className="about-container">
      <div className="about-box">
        <h2 className="about-title">About the Voice Authentication System</h2>
        <p className="about-text">
          This project demonstrates a network security implementation layer using voice biometrics. It aims to provide a more robust and user-friendly authentication method than traditional password-based systems.
        </p>
        <p className="about-text">
          The system captures a user's unique voice patterns to create a "voiceprint," which is then used for authentication. This research explores the effectiveness, security benefits, and limitations of this technology.
        </p>
      </div>
    </div>
  );
};

export default About;
