import React, { useState } from "react";

function Signin({ setToken }) {
  const [username, setUserName] = useState();
  const [password, setPassword] = useState();

  async function loginUser(credentials) {
    return fetch('http://localhost:8080/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(credentials)
    })
      .then(data => data.json())
   }
   
  const handleSubmit = async e => {
    e.preventDefault();
    const token = await loginUser({
      username,
      password
    })
    setToken(token)
   }

  return (
    <>
      <form id="login" onSubmit={handleSubmit}>
        <h1 id="title">Login</h1>
        <input
          type="text"
          placeholder="Username or email"
          onChange={e => setUserName(e.target.value)}
        />
        <br></br>
        <input
          type="password"
          placeholder="Password"
          onChange={e => setPassword(e.target.value)}
        />
        <br></br>
        <button type="submit">Login</button>
      </form>
    </>
  );
}



export default Signin;
