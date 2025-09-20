import React, { useState } from 'react';

export default function Register() {
  const [form, setForm] = useState({ username: "", email: "", password: "" });
  const [message, setMessage] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    // Connect to backend user registration API here
    setMessage("Registration successful!");
  }

  return (
    <form onSubmit={handleSubmit}>
      <h3>Register</h3>
      {message && <p>{message}</p>}
      <input placeholder="Username" value={form.username} onChange={e => setForm({...form, username: e.target.value})} required />
      <input type="email" placeholder="Email" value={form.email} onChange={e => setForm({...form, email: e.target.value})} required />
      <input type="password" placeholder="Password" value={form.password} onChange={e => setForm({...form, password: e.target.value})} required />
      <button type="submit">Register</button>
    </form>
  );
}
