import React, { useState, useRef } from 'react';
import '../styles/VoiceRecorderStyles.css';

const VoiceRecorder = ({ onRecordComplete, buttonText }) => {
  const [isRecording, setIsRecording] = useState(false);
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorderRef.current = new MediaRecorder(stream);
      audioChunksRef.current = [];
      
      mediaRecorderRef.current.ondataavailable = (event) => {
        audioChunksRef.current.push(event.data);
      };
      
      mediaRecorderRef.current.onstop = () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/webm' });
        
        // Convert the Blob to a Base64 string
        const reader = new FileReader();
        reader.onloadend = () => {
          const base64data = reader.result;
          onRecordComplete(base64data);
        };
        reader.readAsDataURL(audioBlob);
      };
      
      mediaRecorderRef.current.start();
      setIsRecording(true);
      console.log("Recording started...");
    } catch (err) {
      console.error('Error accessing microphone:', err);
      alert('Error accessing microphone. Please check permissions.');
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && mediaRecorderRef.current.state === 'recording') {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
      console.log("Recording stopped.");
    }
  };

  return (
    <div className="recorder-container">
      <button 
        className={`record-button ${isRecording ? 'recording' : ''}`} 
        onClick={isRecording ? stopRecording : startRecording}
      >
        {isRecording ? 'Stop Recording' : buttonText}
      </button>
      {isRecording && <div className="recording-status">Recording...</div>}
    </div>
  );
};

export default VoiceRecorder;
