import React from 'react';
import './HighlightText.css';

export default function HighlightText({ text, highlights }) {
  // Split text by highlighted parts (assumed as list of {start, end} indices)
  // For simplicity, assume highlights is list of strings to highlight within text

  if (!highlights?.length) return <p>{text}</p>;

  let parts = [text];
  highlights.forEach((hl) => {
    parts = parts.flatMap((part) => {
      if (typeof part !== 'string') return [part];
      const split = part.split(new RegExp(`(${hl})`, 'gi'));
      return split.map((s) => (s.toLowerCase() === hl.toLowerCase() ? { highlight: true, text: s } : s));
    });
  });

  return (
    <p>
      {parts.map((part, i) =>
        typeof part === 'string' ? (
          <span key={i}>{part}</span>
        ) : (
          <mark key={i} className="highlighted-text" title="Highlighted text">{part.text}</mark>
        )
      )}
    </p>
  );
}
