
import React from 'react';
import './App.css';
import Home from './components/Home.js';
import LoginAndRegistration from './components/Loginandregistration'; 
import Packages from './components/Package';
import PackageDetails from './components/PackageDetails.js';
import Navbar from "./components/NavBar"
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<LoginAndRegistration />} />
        <Route path="/packages" element={<Packages />} />
        <Route path="/package/:id" element={<PackageDetails />} />
      </Routes>
      </div>
    </Router>
  );
}

export default App;

