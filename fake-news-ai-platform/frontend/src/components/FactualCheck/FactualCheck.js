import React from 'react';
import './FactualCheck.css';

export default function FactualCheck({ checks }) {
  if (!checks?.length) return <p>No fact checks available.</p>;

  return (
    <div className="factual-check">
      <ul>
        {checks.map((check, i) => (
          <li key={i}>
            <a href={check.url} target="_blank" rel="noreferrer">{check.headline}</a> - <strong>{check.verdict}</strong> ({check.source})
          </li>
        ))}
      </ul>
    </div>
  );
}
