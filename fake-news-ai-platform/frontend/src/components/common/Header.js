import React from 'react';
import { Link } from 'react-router-dom';

export default function Header() {
  return (
    <header style={{ padding: '10px', backgroundColor: '#007acc', color: 'white' }}>
      <h1>Fake News Detection</h1>
      <nav>
        <Link to="/" style={{ margin: '0 10px', color: 'white' }}>Home</Link>
        <Link to="/analysis" style={{ margin: '0 10px', color: 'white' }}>Analysis</Link>
        <Link to="/learning" style={{ margin: '0 10px', color: 'white' }}>Learning</Link>
        <Link to="/about" style={{ margin: '0 10px', color: 'white' }}>About</Link>
      </nav>
    </header>
  );
}
