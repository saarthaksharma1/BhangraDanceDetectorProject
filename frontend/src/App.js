import './App.css';
import { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('/api/hello')
      .then(res => res.text())
      .then(setMessage)
      .catch(console.error);
  }, []);

  return (
    <div className="App">
      <h1>Flask says:</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
