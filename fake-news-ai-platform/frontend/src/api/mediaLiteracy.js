import client from './client';

export async function deconstructTopic(topic) {
  const response = await client.post('/api/v1/learning/deconstruct', { topic });
  return response.data;
}
