import Image from 'next/image'
import Bargraph from '../components/Bargraph/Bargraph'
import React, { useMemo } from 'react';

export default function Data() {
  return (
    <div className="
      w-full
      pt-24
      flex
      flex-col
      justify-center
      items-center

    ">
      <h1 className="mb-4 pb-10 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white" >
        <span className="underline underline-offset-3 decoration-8 decoration-blue-400 dark:decoration-blue-600">
          Bar Chart
        </span>  
      </h1>   
      <div className="
        flex
        flex-col
        sm:flex-col
        xl:flex-row
        sm:items-center
        xl:items-start
        p-10
      ">
        <div >
          <Bargraph top={10} right={50} bottom={50} left={50} width={900} height={400} fill="tomato" file="/finaldata/barByYear.csv" xaxis='Year' yaxis='Frequency'/>
        </div>
        <div className="sm:text-center xl:text-left">
          <h1 className='mb-2 pb-5 text-xl font-extrabold leading-none tracking-tight text-gray-900 md:text-3xl lg:text-4xl dark:text-white hover:text-blue-400'>
            <a href="/">
              Search Queries
            </a>   
          </h1>
        </div>
        
      </div> 
      
    </div>
  )
}