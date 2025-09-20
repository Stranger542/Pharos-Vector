import client from './client';

export async function analyzeArticle(text) {
  const response = await client.post('/api/v1/fake-news/predict', { text });
  return response.data;
}
