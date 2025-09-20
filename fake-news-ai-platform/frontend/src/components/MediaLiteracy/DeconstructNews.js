import React from 'react';

export default function DeconstructNews({ topic }) {
  const questions = [
    `Who created this message about ${topic}?`,
    "What techniques are used to attract attention?",
    "Is this fact, opinion, or something else?",
    "Can you find alternate sources to verify?"
  ];

  return (
    <div>
      <h3>Deconstruct the News - Guided Analysis</h3>
      <ul>
        {questions.map((q, i) => (
          <li key={i}>{q}</li>
        ))}
      </ul>
    </div>
  );
}
