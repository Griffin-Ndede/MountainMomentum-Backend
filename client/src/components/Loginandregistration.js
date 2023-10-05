import React, { useState } from "react";

const LoginAndRegistration = () => {
  const [isLogin, setIsLogin] = useState(true);
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
  });

  const handleToggleAuth = () => {
    setIsLogin(!isLogin);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle login or sign-up logic here using formData.
    // For a real application, you would send a request to your backend.

    console.log(formData);
  };

  return (
    <div className="login-registration-container">
      <div>
        <h2>
          {isLogin ? "Log In" : "Sign Up"}
        </h2>
        <form onSubmit={handleSubmit}>
          {!isLogin && (
            <div className="input-container">
              <label htmlFor="username">
                Username
              </label>
              <input
                type="text"
                id="username"
                name="username"
                onChange={handleChange}
                value={formData.username}
                className="input-field"
              />
            </div>
          )}
          <div className="input-container">
            <label htmlFor="email">
              Email
            </label>
            <input
              type="email"
              id="email"
              name="email"
              onChange={handleChange}
              value={formData.email}
              className="input-field"
            />
          </div>
          <div className="input-container">
            <label htmlFor="password">
              Password
            </label>
            <input
              type="password"
              id="password"
              name="password"
              onChange={handleChange}
              value={formData.password}
              className="input-field"
            />
          </div>
          <div className="button-container">
            <button type="submit" className="submit-button">
              {isLogin ? "Log In" : "Sign Up"}
            </button>
            <button
              type="button"
              onClick={handleToggleAuth}
              className="toggle-button"
            >
              {isLogin ? "Don't have an account? Sign Up" : "Already have an account? Log In"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginAndRegistration;
