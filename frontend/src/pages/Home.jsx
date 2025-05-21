import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div className="home">
      <h1>🏠 Welcome to Bhangra Detector</h1>
      <p>Click below to test your moves!</p>
      <Link to="/page2">
        <button>Start Detection</button>
      </Link>
    </div>
  );
}
