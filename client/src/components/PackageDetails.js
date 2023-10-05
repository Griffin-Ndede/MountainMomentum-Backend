// import React from 'react';
// import { useParams } from 'react-router-dom';

// const PackageDetails = ({ packagesData }) => {
//   const { id } = useParams(); // Get the package id from the URL parameter

//   // Find the selected package
//   const selectedPackage = packagesData.find(pkg => pkg.id === parseInt(id));

//   // Check if selectedPackage exists
//   if (!selectedPackage) {
//     return <div>Package not found</div>;
//   }

//   return (
//     <div className='package-details'>
//       <h2>{selectedPackage.title}</h2>
//       <div className='package-card'>
//         <div className='package-card-content'>
//           <h2>{selectedPackage.title}</h2>
//           <img src={selectedPackage.imageUrl} alt={selectedPackage.title} />
//           <p>{selectedPackage.description}</p>
//           <p>Additional Text</p>
//         </div>
//       </div>
//     </div>
//   );
// }

// export default PackageDetails;
