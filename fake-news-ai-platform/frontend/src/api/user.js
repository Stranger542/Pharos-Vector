import client from './client';

export async function getUserProfile(username) {
  const response = await client.post('/api/v1/user/profile', { username });
  return response.data;
}
