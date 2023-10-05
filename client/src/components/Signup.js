// import React, { useState } from "react";

// function Signup() {
//   const [username, setUsername] = useState("Guest");

//   function handleSubmit(event) {
//     event.preventDefault();
//     console.log("content submitted");
//   }

//   return (
//     <>
//       <h1 id="register">Create account</h1>
//       <p id="register">Welcome, {username}</p>

//       <form>
//         <input
//           type="text"
//           placeholder="username"
//           onChange={(event) => setUsername(event.target.value)}
//         />
//         <br></br>
//         <input
//           type="text"
//           placeholder="email address"
//           onChange={(event) => console.log(event.target.value)}
//         />
//         <br></br>
//         <input
//           type="password"
//           placeholder="Create password"
//           onChange={(event) => console.log(event.target.value)}
//         />
//         <br></br>
//         <input
//           type="text"
//           placeholder="first name"
//           onChange={(event) => console.log(event.target.value)}
//         />
//          <input
//           type="text"
//           placeholder="last name"
//           onChange={(event) => console.log(event.target.value)}
//         />
//         <br></br>
//         <button type="submit" onClick={handleSubmit}>
//           Create account
//         </button>
//       </form>
//     </>
//   );
// }

// export default Signup;
import React, { useState } from "react";

function Signup() {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    first_name: "",
    last_name: "",
  });

  async function handleSubmit(event) {
    event.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.status === 200) {
        // Registration was successful
        console.log("Registration successful");
        // You can perform further actions here, such as redirecting the user.
      } else {
        const data = await response.text();
        // Registration failed
        console.error(data);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  }

  function handleInputChange(event) {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  }

  return (
    <>
      <h1 id="register">Create account</h1>
      <p id="register">Welcome, {formData.username}</p>

      <form>
        <input
          type="text"
          name="username"
          placeholder="username"
          onChange={handleInputChange}
        />
        <br></br>
        <input
          type="text"
          name="email"
          placeholder="email address"
          onChange={handleInputChange}
        />
        <br></br>
        <input
          type="password"
          name="password"
          placeholder="Create password"
          onChange={handleInputChange}
        />
        <br></br>
        <input
          type="text"
          name="first_name"
          placeholder="first name"
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="last_name"
          placeholder="last name"
          onChange={handleInputChange}
        />
        <br></br>
        <button type="submit" onClick={handleSubmit}>
          Create account
        </button>
      </form>
    </>
  );
}

export default Signup;

