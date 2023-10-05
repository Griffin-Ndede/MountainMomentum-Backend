
import React from 'react';
import './App.css';
import Home from './components/Home.js';
// import LoginAndRegistration from './components/Loginandregistration'; 
import PackageDetails from './components/PackageDetails.js';
import Navbar from "./components/NavBar"
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import AuthenticationPage from './components/AuthPage';
import Footer from './components/Footer';
import About from './components/About';


function App() {
  return (
    <BrowserRouter>
    <Navbar/>
      <div>
      <Routes>
        <Route path="/" element={<Home />} />
        {/* <Route path="/login" element={<LoginAndRegistration />} /> */}
        <Route path='/login' element= {<AuthenticationPage/>}/>
        <Route path="/package/:id" element={<PackageDetails />} />
        <Route path='/about' element= {<About/>}/>
      </Routes>
      </div>
      <Footer/>
    </BrowserRouter>
  );
}

export default App;

