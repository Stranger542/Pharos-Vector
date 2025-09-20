import React from 'react';

export default function CredibilityCoach({ userStats }) {
  // Example personalized messages based on user's activity
  if (!userStats) return null;

  return (
    <div>
      <h3>Your Credibility Coach</h3>
      <p>You've completed {userStats.totalQuizzes} quizzes.</p>
      <p>Keep practicing to spot logical fallacies and misinformation techniques more easily!</p>
    </div>
  );
}
