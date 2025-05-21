import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';

function Home() {
  return (
    <div style={{ textAlign: 'center', marginTop: 50 }}>
      <h1>🏠 Welcome to Bhangra Detector</h1>
      <p>Click below to test your moves!</p>
      <Link to="/page2">
        <button style={{ padding: '10px 20px', fontSize: 16 }}>
          Start Detection
        </button>
      </Link>
    </div>
  );
}

function Page2() {
  return (
    <div style={{ textAlign: 'center', marginTop: 50 }}>
      <h1>🎬 Detection Page</h1>
      <p>Here we’ll run your dance detector.</p>
      <Link to="/">
        <button style={{ padding: '10px 20px', fontSize: 16 }}>
          Back to Home
        </button>
      </Link>
    </div>
  );
}

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/page2" element={<Page2 />} />
    </Routes>
  );
}
