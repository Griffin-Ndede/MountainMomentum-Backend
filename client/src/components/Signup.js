import { useState } from "react";
// import { useNavigate } from "react-router-dom";
// import SweetAlert2 from "sweetalert2";

function Signup() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    first_name: '',
    last_name:'',

  });

 
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:5000/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      if (response.status === 200) {
        alert('Account created successfully!');
        // Redirect to login or other page
      } else {
        alert('Registration failed.');
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
