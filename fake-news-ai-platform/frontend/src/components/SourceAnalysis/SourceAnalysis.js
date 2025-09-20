import React from 'react';
import './SourceAnalysis.css';

export default function SourceAnalysis({ source }) {
  if (!source) return null;

  return (
    <div className="source-analysis">
      <h3>Source: {source.domain}</h3>
      <p><strong>Trust Score:</strong> {source.trust_score}</p>
      <p>{source.reputation_summary}</p>
    </div>
  );
}
