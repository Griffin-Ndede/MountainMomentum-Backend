import React, { useState } from "react";
import Signin from "./Signin";
import Signup from "./Signup";

function AuthenticationPage() {
  const [isSignIn, setIsSignIn] = useState(true);

  const togglePage = () => {
    setIsSignIn(!isSignIn);
  };

  return (
    <div className="loginpage">
    <div id="authpage">
      {isSignIn ? <Signin /> : <Signup />}
      <button onClick={togglePage}>
        {isSignIn
          ? "Don't have an account? Create account"
          : "Already have an account? Log in"}
      </button>
    </div>
    </div>
    
  );
}

export default AuthenticationPage;
