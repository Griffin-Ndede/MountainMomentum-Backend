import React from 'react';
function AboutUs() {
  const imageStyles = {
    width: '150px', // Set the desired width here
    height: 'auto', // Maintain aspect ratio
    borderRadius: '50%', // Rounded shape for circular avatars
  };
  return (
    <div>
      <div className="jumbotron">
        <div className="container">
          <h1 className="display-4">Welcome to Mountain Momentum</h1>
          <p className="lead">Explore nature, connect with fellow hikers, and experience unforgettable adventures with us.</p>
        </div>
      </div>
      <div className="container">
        <h2 className="text-center mb-4">ABOUT US</h2>
        <p className="lead">Mountain Momentum is a company dedicated to keeping Kenyans connected through traversing our beautiful land. We strive to help our clients grow and achieve new heights by ensuring that they are connected to enable them to participate in the exponential opportunities for innovation in the vibrant Kenyan community.</p>
      </div>
      <div className="container">
        <h2 className="text-center mb-4">OUR TEAM</h2>
        <p className="lead">Our team is dedicated to providing exemplary service delivery to our clients. We believe in treating each and every customer like a V.I.P and ensuring their needs are met in a timely manner. We assure the quality of service delivery while maintaining industry standards.</p>
        <div className="row">
        <div className="team-members">
  <div className="col-md-4 team-member">
    <img src="https://as1.ftcdn.net/v2/jpg/02/30/60/82/1000_F_230608264_fhoqBuEyiCPwT0h9RtnsuNAId3hWungP.jpg" alt="Peter Griffin" className="img-fluid rounded-circle mb-3" style={imageStyles} />
    <h3>Peter Griffin</h3>
    <p>CEO</p>
    <p>Peter is our visionary leader and the driving force behind our hiking adventures. 
       With a deep passion for the great outdoors, he inspires our team and fellow hikers to explore the most breathtaking trails. 
       Peter's leadership ensures that every hiking experience is well-organized and filled with unforgettable moments.</p>
  </div>
  <div className="col-md-4 team-member">
    <img src="https://static.vecteezy.com/system/resources/previews/014/212/681/original/female-user-profile-avatar-is-a-woman-a-character-for-a-screen-saver-with-emotions-for-website-and-mobile-app-design-illustration-on-a-white-isolated-background-vector.jpg" alt="Ubah" className="img-fluid rounded-circle mb-3" style={imageStyles}/>
    <h3>Ubah</h3>
    <p>Event Coordinator</p>
    <p>Shadrack is our event coordinator, specializing in crafting amazing hiking events that bring hikers together. 
       His attention to detail ensures that every hike is a seamless and enjoyable experience.
       With Shadrack's guidance, you can expect well-planned adventures and exciting surprises along the trail.</p>
  </div>
  <div className="col-md-4 team-member">
    <img src="https://static.vecteezy.com/system/resources/previews/002/002/403/original/man-with-beard-avatar-character-isolated-icon-free-vector.jpg" alt="Brian Kibet" className="img-fluid rounded-circle mb-3" style={imageStyles}/>
    <h3>Brian Kibet</h3>
    <p>Trail Guide</p>
    <p>Brian, our experienced trail guide, leads hikers through the most scenic and challenging routes. 
       His extensive knowledge of the wilderness and hiking techniques ensures your safety and enriches your hiking journey. 
       Brian's passion for nature and storytelling will make your hikes educational and unforgettable.</p>
  </div>
</div>

        </div>
      </div>
    </div>
  );
}

export default AboutUs;
