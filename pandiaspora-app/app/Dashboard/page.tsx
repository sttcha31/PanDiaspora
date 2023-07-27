import Image from 'next/image'
import Bargraph from '../components/Bargraph/Bargraph'
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
      <Bargraph top={10} right={50} bottom={50} left={50} width={900} height={400} fill="tomato" file="/finaldata/barByYear.csv" xaxis='Year' yaxis='Frequency'/>
    </div>
  )
}