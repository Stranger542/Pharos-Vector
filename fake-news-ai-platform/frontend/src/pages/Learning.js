import React from 'react';
import Layout from '../components/common/Layout';
import DeconstructNews from '../components/MediaLiteracy/DeconstructNews';
import FallacyFinder from '../components/MediaLiteracy/FallacyFinder';
import CredibilityCoach from '../components/MediaLiteracy/CredibilityCoach';

export default function Learning() {
  const userStats = { totalQuizzes: 5, correctAnswers: 4 };

  return (
    <Layout>
      <h2>Media Literacy Hub</h2>
      <DeconstructNews topic="Fake News" />
      <FallacyFinder />
      <CredibilityCoach userStats={userStats} />
    </Layout>
  );
}
