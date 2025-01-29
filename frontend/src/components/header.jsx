import React from 'react'
import myImage from '../assets/avion.jpg';
export default function header() {
  return (
    <div>
        <section className="flex flex-col lg:flex-row items-center justify-between px-4 sm:px-8 lg:px-16 xl:px-24 py-8 gap-3 text-gray-900">
      <div className="w-full lg:w-1/2 flex flex-col items-start text-center lg:text-left ">
        <div className="space-y-6 lg:space-y-8">
          <h2 className="block w-full uppercase text-2xl sm:text-4xl font-thin text-slate-950">
            Construire aujourd'hui pour un avenir durable
          </h2>
          <p className="sm:text-lg text-base text-gray-500">
            Nous nous engageons à offrir une expertise diversifiée dans divers
            secteurs, avec un accent sur la qualité, l'intégrité, et la
            satisfaction des besoins de nos clients, tout en respectant les
            délais et l'environnement.
          </p>
          <div className="flex justify-center lg:justify-normal">
            <a
              to="/contact"
              className="flex items-center px-4 py-3 mb-3 sm:px-6 sm:py-2 text-white bg-slate-800 rounded-sm sm:mb-0 hover:bg-slate-900 sm:w-auto transition"
            >
              Nous contacter
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="w-4 h-4 ml-2"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <line x1="5" y1="12" x2="19" y2="12"></line>
                <polyline points="12 5 19 12 12 19"></polyline>
              </svg>
            </a>
 
            <a
              to="/shop"
              className="flex items-center px-6 py-3 mb-3 rounded-md sm:mb-0 sm:w-auto mx-2 text-gray-600 border border-slate-300 hover:border-slate-400 transition"
            >
              Nos matériaux
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="w-4 h-4 ml-2"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <line x1="5" y1="12" x2="19" y2="12"></line>
                <polyline points="12 5 19 12 12 19"></polyline>
              </svg>
            </a>
          </div>
        </div>
      </div>
 
      <div className="w-full lg:w-1/2 flex justify-center items-center p-0 sm:p-4">
        <div className="w-full max-w-md md:max-w-lg lg:max-w-xl">
          <img
            src={myImage}
            alt="Illustration d'équipe de travail"
            className="w-full object-cover rounded-md shadow-md"
          />
        </div>
      </div>
    </section>
    </div>
  )
}
