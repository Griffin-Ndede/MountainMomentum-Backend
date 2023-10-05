// import { useState } from "react";
// import { useNavigate } from "react-router-dom";
// import SweetAlert2 from "sweetalert2";
// import Spinner from "../components/Spinner";

// function Signup() {
//     const navigate = useNavigate();

//     const [isLoading, setIsLoading] = useState(false);
//     const [errors, setErrors] = useState({}); 
//     const [formData, setFormData] = useState({
//     username: "",
//     email: "",
//     password: "",
//     first_name: "",
//     last_name: "",
//   });

//   const handleSubmit = async (event) => {
//     event.preventDefault();

//     try {
//       let response = await fetch("http://127.0.0.1:5000/register", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         body: JSON.stringify(formData),
//       });

//       if (response.ok) {
//         setIsLoading(true); // set loading to true
//         setTimeout(() => {
//           setIsLoading(false); // set it to false after 2 secs and direct this to login page
//           SweetAlert2.fire({
//             title: "Success!",
//             text: "Registration to watamu foods is successfull, login to continue",
//             icon: "success",
//             confirmButtonText: "Cool",
//             confirmButtonColor: "#f1cc17",
//           });
//           navigate("/login");
//         }, 1500);
//       } else {
//         let error_data = await response.json();
//         setErrors(error_data.message);
//       }
//     } catch (error) {
//       console.error("Network error:", error);
//     }
//   };

//   const handleInputChange = (e) => {
//     const { name, value } = e.target;
//     setFormData((prevFormData) => ({
//       ...prevFormData,
//       [name]: value,
//     }));
//   };

//   return (
//     <>
//       <h1 id="register">Create account</h1>
//       <p id="register">Welcome, {formData.username}</p>

//       <form>
//         <input
//           type="text"
//           name="username"
//           placeholder="username"
//           onChange={handleInputChange}
//         />
//         <br></br>
//         <input
//           type="text"
//           name="email"
//           placeholder="email address"
//           onChange={handleInputChange}
//         />
//         <br></br>
//         <input
//           type="password"
//           name="password"
//           placeholder="Create password"
//           onChange={handleInputChange}
//         />
//         <br></br>
//         <input
//           type="text"
//           name="first_name"
//           placeholder="first name"
//           onChange={handleInputChange}
//         />
//         <input
//           type="text"
//           name="last_name"
//           placeholder="last name"
//           onChange={handleInputChange}
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
import { useNavigate } from "react-router-dom";
import SweetAlert2 from "sweetalert2";
import Spinner from "./spinner";

export default function Register() {
  const navigate = useNavigate();

  const [isLoading, setIsLoading] = useState(false);
  const [errors, setErrors] = useState({});
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    phonenumber: "",
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      let resp = await fetch("http://localhost:5000/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (resp.ok) {
        setIsLoading(true); // set loading to true
        setTimeout(() => {
          setIsLoading(false); // set it to false after 2 secs and direct this to login page
          SweetAlert2.fire({
            title: "Success!",
            text: "New user successfully registered, login to continue",
            icon: "success",
            confirmButtonText: "Cool",
            confirmButtonColor: "#f1cc17",
          });
          navigate("/login");
        }, 1500);
      } else {
        let errorData = await resp.json();
        setErrors(errorData.message);
      }
    } catch (error) {
      console.error("Network error:", error);
    }
  };

  return (
    <>
      <h1 id="register">Create account</h1>
      <p id="register">Welcome, {formData.username}</p>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="username"
          onChange={handleInputChange}
        />
        <br />
        <input
          type="text"
          name="email"
          placeholder="email address"
          onChange={handleInputChange}
        />
        <br />
        <input
          type="password"
          name="password"
          placeholder="Create password"
          onChange={handleInputChange}
        />
        <br />
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

        {isLoading ? (
          <Spinner />
        ) : (
          <button
            type="submit"
            className="block w-full bg-yellow-500 mt-4 py-2 rounded-2xl text-white font-semibold mb-2"
          >
            Register
          </button>
        )}
      </form>
    </>
  );
}



