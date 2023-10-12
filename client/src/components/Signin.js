// import React, { useState } from "react";

// function Signin() {
//   const [username, setUserName] = useState('');
//   const [password, setPassword] = useState('');

//   async function loginUser(credentials) {
//     try {
//       const response = await fetch('http://127.0.0.1:5000/login', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(credentials),
//       });

//       if (response.status === 200) {
//         alert('Login successful');
//       } else {
//         alert('Login failed');
//       }
//     } catch (error) {
//       console.error('Error:', error);
//       alert('An error occurred during login');
//     }
//   }
  
//   const handleSubmit = async e => {
//     e.preventDefault();
//     await loginUser({
//       username,
//       password
//     });
//   }

//   return (
//     <form id="login" onSubmit={handleSubmit}>
//       <h1 id="title">Login</h1>
//       <input
//         type="text"
//         placeholder="Username"
//         onChange={e => setUserName(e.target.value)}
//       />
//       <br></br>
//       <input
//         type="password"
//         placeholder="Password"
//         onChange={e => setPassword(e.target.value)}
//       />
//       <br></br>
//       <button type="submit">Login</button>
//     </form>
//   );
// }

// export default Signin;
import React, { useState } from "react";

function Signin() {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      if (response.status === 200) {
        alert('Login successful');
        // Redirect to your dashboard or another page
      } else {
        alert('Login failed. Please check your credentials.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  return (
    <>
      <h1 id="login">Login</h1>
      <form>
        <input
          type="text"
          name="username"
          placeholder="Username"
          onChange={handleInputChange}
        />
        <br></br>
        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleInputChange}
        />
        <br></br>
        <button type="submit" onClick={handleSubmit}>
          Login
        </button>
      </form>
    </>
  );
}

export default Signin;
