
import React, {useEffect, useState}from 'react';


function Home() {
const [hikes, setHikes] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/hikes")
    .then(response => response.json())
    .then(data =>setHikes(data) )
    .catch(error => console.error("Error fetching data", error))
  }, [])
  return (
    <div>
      <link rel="stylesheet" href="https://demos.creative-tim.com/notus-js/assets/styles/tailwind.css" />
      <link rel="stylesheet" href="https://demos.creative-tim.com/notus-js/assets/vendor/@fortawesome/fontawesome-free/css/all.min.css" />

      <section className="relative bg-blueGray-50">
        <div className="relative pt-16 pb-32 flex content-center items-center justify-center min-h-screen-75">
          <div className="absolute top-0 w-full h-full bg-center bg-cover" style={{
            backgroundImage: "url('https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Mount_Kenya.jpg/1200px-Mount_Kenya.jpg')"
          }}>
            <span id="blackOverlay" className="w-full h-full absolute opacity-75 bg-black"></span>
          </div>
          <div className="container relative mx-auto">
            <div className="items-center flex flex-wrap">
              <div className="w-full lg:w-6/12 px-4 ml-auto mr-auto text-center">
                <div className="pr-12">
                  <h1 className="text-white font-semibold text-5xl">
                    Mountain Momentum.
                  </h1>
                  <p className="mt-4 text-lg text-blueGray-200">
                    The mountain is calling and I have to go.
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div className="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden h-70-px" style={{ transform: "translateZ(0px)" }}>
            <svg className="absolute bottom-0 overflow-hidden" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" version="1.1" viewBox="0 0 2560 100" x="0" y="0">
              <polygon className="text-blueGray-200 fill-current" points="2560 0 2560 100 0 100"></polygon>
            </svg>
          </div>
        </div>
        <section className="pb-10 bg-blueGray-200 -mt-24">
          <div className="container mx-auto px-4">
            <div className="flex flex-wrap">
              <div className="lg:pt-12 pt-6 w-full md:w-4/12 px-4 text-center">
                <div className="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg">
                  <div className="px-4 py-5 flex-auto">
                    <div className="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-red-400">
                      {/* <i className="fas fa-award"></i> */}
                    </div>
                    <h6 className="text-xl font-semibold">Improve your fitness</h6>
                    <p className="mt-2 mb-4 text-blueGray-500">
                    Hiking engages various muscles and enhances cardiovascular health, promoting overall fitness.
                    </p>
                  </div>
                </div>
              </div>
              <div className="w-full md:w-4/12 px-4 text-center">
                <div className="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg">
                  <div className="px-4 py-5 flex-auto">
                    <div className="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-lightBlue-400">
                      {/* <i className="fas fa-retweet"></i> */}
                    </div>
                    <h6 className="text-xl font-semibold">Reduce stress</h6>
                    <p className="mt-2 mb-4 text-blueGray-500">
                    Time spent in nature while hiking reduces stress, anxiety, and depression, improving mental well-being.
                    </p>
                  </div>
                </div>
              </div>
              <div className="pt-6 w-full md:w-4/12 px-4 text-center">
                <div className="relative flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg">
                  <div className="px-4 py-5 flex-auto">
                    <div className="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-emerald-400">
                      {/* <i className="fas fa-fingerprint"></i> */}
                    </div>
                    <h6 className="text-xl font-semibold">Connect with nature</h6>
                    <p className="mt-2 mb-4 text-blueGray-500">
                    Hiking fosters a deeper appreciation for the environment and encourages adventure and exploration.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </section>
      <section>
        <div className='hikes'>
          <ul id='cards'>
            {hikes.map((hike) =>(
              <li id='details' key={hike.id}>
                <img src ={hike.image} alt = {hike.name}></img>
                <h3>{hike.name}</h3>
                <h3>Distance: {hike.distance}</h3>
                <h3>Difficulty: {hike.difficulty}</h3>
              </li>
            ))}
          </ul>
        </div>
      </section>
      <section id='footer'>
      <footer className="footer">
      <div className="footer-content">
        <div className="footer-section about">
          <h2>About Us</h2>
          <p>
          We are passionate hikers, adventurers, and nature enthusiasts. 
          Our mission is to inspire and guide you through unforgettable hiking experiences, 
          from breathtaking trails to expert tips. 
          Join us on a journey to discover the wonders of the great outdoors.
          </p>
        </div>
        <div className="footer-section contact">
          <h2>Contact Us</h2>
          <address>
            <p>Email: mountainmomentum@gmail.com</p>
            <p>Phone: +2547 123 456 789</p>
          </address>
        </div>
        <div className="footer-section links">
          <h2>Quick Links</h2>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/services">Services</a></li>
            <li><a href="/contact">Contact</a></li>
          </ul>
        </div>
      </div>
      <div className="footer-bottom">
        <p>&copy; 2023 Mountain Momentum</p>
      </div>
    </footer>
      </section>
    </div>
  );
}

export default Home;
