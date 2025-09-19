import React from 'react';
import './CredibilityReport.css';

export default function CredibilityReport({ report }) {
  if (!report) return null;

  return (
    <div className="credibility-report">
      <h2>Overall Credibility: {report.score} / 100 ({report.label})</h2>
      <p>{report.summary}</p>

      <section>
        <h3>Source Analysis</h3>
        <p>Trust Score: {report.source.trust_score}</p>
        <p>{report.source.summary}</p>
      </section>

      <section>
        <h3>Factual Cross-Check</h3>
        <ul>
          {report.factual_checks.map((check, i) => (
            <li key={i}>
              <a href={check.url} target="_blank" rel="noreferrer">{check.headline}</a> - {check.verdict}
            </li>
          ))}
        </ul>
      </section>

      <section>
        <h3>Content Highlights</h3>
        {report.highlights.map((highlight, i) => (
          <span key={i} className="highlight" title={highlight.explanation}>
            {highlight.text}
          </span>
        ))}
      </section>
    </div>
  );
}
