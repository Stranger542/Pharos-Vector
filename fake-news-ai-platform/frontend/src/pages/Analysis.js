import React, { useState } from 'react';
import Layout from '../components/common/Layout';
import CredibilityReport from '../components/CredibilityReport/CredibilityReport';
import { analyzeArticle } from '../api/fakeNews';

export default function Analysis() {
  const [text, setText] = useState('');
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleAnalyze() {
    setLoading(true);
    const data = await analyzeArticle(text);
    setReport(data);
    setLoading(false);
  }

  return (
    <Layout>
      <h2>Analyze a News Article</h2>
      <textarea
        rows={8}
        cols={80}
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste news article text here..."
      />
      <br />
      <button onClick={handleAnalyze} disabled={loading || !text.trim()}>
        {loading ? 'Analyzing...' : 'Analyze'}
      </button>
      {report && <CredibilityReport report={report} />}
    </Layout>
  );
}
