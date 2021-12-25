import React from 'react';
import { ChevronLeftIcon, ChevronRightIcon } from '@heroicons/react/solid'

const Pagination = ({ assetsPerPage, totalAssets, paginate, currentPage }) => {
  const pageNumbers = [];

  for (let i = 1; i <= Math.ceil(totalAssets / assetsPerPage); i++) {
    pageNumbers.push(i);
  }

  
  return (
    <nav>
      <ul className='pagination'>
        {pageNumbers.map(number => (
          <li key={number} className='page-item'>
            <a onClick={() => paginate(number)} href='#' className='page-link'>
              {number}
            </a>
          </li>
        ))}
      </ul>
    </nav>


  //   <div className="bg-white px-4 py-3 flex items-center justify-between border-t border-gray-200 sm:px-6">
  //   <div className="flex-1 flex justify-between sm:hidden">
  //     <a
  //       href="#"
  //       className="relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
  //     >
  //       Previous
  //     </a>
  //     <a
  //       href="#"
  //       className="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50"
  //     >
  //       Next
  //     </a>
  //   </div>
  //   <div className="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
  //     <div>
  //       <p className="text-sm text-gray-700">
  //         Showing <span className="font-medium">{currentPage}</span> to <span className="font-medium">{pageNumbers.slice(-1)}</span> of{' '}
  //         <span className="font-medium">{totalAssets}</span> results
  //       </p>
  //     </div>
  //     <div>
  //       <nav className="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
  //         <a
  //           href="#"
  //           className="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
  //         >
  //           <span className="sr-only">Previous</span>
  //           <ChevronLeftIcon className="h-5 w-5" aria-hidden="true" />
  //         </a>
  //         {/* Current: "z-10 bg-indigo-50 border-indigo-500 text-indigo-600", Default: "bg-white border-gray-300 text-gray-500 hover:bg-gray-50" */}
          
  //         {pageNumbers.map(number => (
  //           <li key = {number} className='page-item'>
  //             <a
  //               onClick={() => paginate(number)} 
  //               href="#"
  //               className="bg-white border-gray-300 text-gray-500 hover:bg-gray-50 relative inline-flex items-center px-4 py-2 border text-sm font-medium"
  //             >
  //               {number}
  //             </a>
  //           </li>
  //         ))}

  //         {/* <a
  //           href="#"
  //           aria-current="page"
  //           className="z-10 bg-indigo-50 border-indigo-500 text-indigo-600 relative inline-flex items-center px-4 py-2 border text-sm font-medium"
  //         >
  //           1
  //         </a> */}
          

  //         <a
  //           href="#"
  //           className="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
  //         >
  //           <span className="sr-only">Next</span>
  //           <ChevronRightIcon className="h-5 w-5" aria-hidden="true" />
  //         </a>
  //       </nav>
  //     </div>
  //   </div>
  // </div>
  );
};

export default Pagination;