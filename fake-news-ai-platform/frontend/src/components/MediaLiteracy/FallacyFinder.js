import React, { useState } from 'react';

const sampleQuestions = [
  {
    text: "The politician is corrupt because he once said something controversial.",
    correct: "Ad Hominem",
    options: ["Ad Hominem", "Straw Man", "False Dilemma", "Hasty Generalization"]
  },
  {
    text: "Either we ban all social media or society will collapse.",
    correct: "False Dilemma",
    options: ["Ad Hominem", "Straw Man", "False Dilemma", "Hasty Generalization"]
  }
];

export default function FallacyFinder() {
  const [score, setScore] = useState(0);
  const [currentQ, setCurrentQ] = useState(0);

  function handleAnswer(option) {
    if (option === sampleQuestions[currentQ].correct) {
      setScore(score + 1);
    }
    setCurrentQ(currentQ + 1);
  }

  if (currentQ >= sampleQuestions.length) {
    return <div>Quiz complete! Your score: {score} / {sampleQuestions.length}</div>;
  }

  const q = sampleQuestions[currentQ];

  return (
    <div>
      <h3>Identify the Logical Fallacy</h3>
      <p>{q.text}</p>
      <ul>
        {q.options.map((opt, i) => (
          <li key={i}>
            <button onClick={() => handleAnswer(opt)}>{opt}</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
