import React , {useEffect, useState} from 'react'
import './itenary.css'
const Recommends = ({name}) => {
    
   
      useEffect(() => {
        getGoals();
        loadData();
        // console.log("hellooo");
        //setInterval(loadData(), 10000000000);
      });

      // const [n1,setn1]
      const [objects,setObjects] = useState([]);
      // setObjects([...object]);

      const getGoals =  async () => {
        try {
          const res = await fetch('https://30ef-2401-4900-4e20-cdd5-2080-b3b9-e510-b051.in.ngrok.io/test');
          const blocks = await res.json();
          console.log(blocks);
          setObjects(blocks.result);
          
        } catch (e) {
          console.log(e);
        }
      }

    const loadData = async () => {
        try {
          const res = await fetch('https://30ef-2401-4900-4e20-cdd5-2080-b3b9-e510-b051.in.ngrok.io/goals');
          const blocks = await res.json();
          console.log(blocks)
        } catch (e) {
          console.log(e);
        }
      }
  return (
    <>
    
        <div className='recommendItems'style={{color:"white"}}>
            List of goals 
            
        </div>
        {objects.map(object => {
          return <div className='goals'>{object.name}</div>
        }

        )}
  
    </>
  )
}

export default Recommends