import React, { useRef, useState } from 'react'

import NavBar from './NavBar';
import './../style/Location.css'
//import { Search, GpsFixed } from "@material-ui/icons"
//import './../style/Home.css'
import { useEffect } from "react";

//import Iternary from '../comps/Iternary';
// import Recommends from '../pages/comps/Recommends';
import Maps from '../pages/comps/Map.js';
import { geocodeByAddress } from "react-places-autocomplete";
import axios from 'axios';
import { useHistory } from "react-router-dom";
import Data from './../config';

import qs from 'qs';

const directionsService = new window.google.maps.DirectionsService;

const url = Data['url'];
export default function Rewards() {

    const [sourceCors, setSource] = useState({ lat: '', lon: '' });
    const [destinationCors, setDestination] = useState({ lat: '', lon: '' });
    const [directionsRes, setdirectionsRes] = useState();
    //const [selectedEmotion, setselectedEmotion] = useState('happy');
    const [video, setVideo] = useState();
    const sourceRef = useRef();
    const [objects,setObjects] = useState([]);
    const destinationRef = useRef();
    const history = useHistory();


    const [Apiresponse, setApiresponse] = useState();

    const handleSubmit = () => {

        let inputSourceText = sourceRef.current.value;
        let inputDestinationText = destinationRef.current.value;

        getDirections({ source: inputSourceText, destination: inputDestinationText })

        //below code gets lat and long for input places
        geocodeByAddress(inputSourceText)
            .then(results => setSource({
                lat: results[0].geometry.location.lat(),
                lon: results[0].geometry.location.lng()
            }))
            .catch(error => console.error(error));

        geocodeByAddress(inputDestinationText)
            .then(results => setDestination({
                lat: results[0].geometry.location.lat(),
                lon: results[0].geometry.location.lng()
            }))
            .catch(error => console.error(error));

    }


    async function getDirections({ source, destination }) {
        const res = await directionsService.route({
            origin: source,
            destination: destination,
            travelMode: window.google.maps.TravelMode.DRIVING
        })
        setdirectionsRes(res);
    }
    const getGoals =  async () => {
        try {
        //   const res = await fetch('https://30ef-2401-4900-4e20-cdd5-2080-b3b9-e510-b051.in.ngrok.io/test');
        //   const blocks = await res.json();
        //   console.log(blocks);
        //   setObjects(blocks.result);
          
        } catch (e) {
          console.log(e);
        }
      }

    const loadData = async () => {
        try {
        //   const res = await fetch('https://30ef-2401-4900-4e20-cdd5-2080-b3b9-e510-b051.in.ngrok.io/goals');
        //   const blocks = await res.json();
        //   console.log(blocks)
        } catch (e) {
          console.log(e);
        }
      }
      const [goalItem,setGoalItem] = useState([]);
      const [locationItem, setLocationItem] = useState([]);
    useEffect(() => {
        getGoals();
        loadData();
        if (destinationCors.lat != '' && sourceCors.lat != '') {
            const params = new URLSearchParams()
            params.append('slat', sourceCors.lat)
            params.append('slong', sourceCors.lon)
            params.append('dlat', destinationCors.lat)
            params.append('dlong', destinationCors.lon)

            //params.append('mood', selectedEmotion)
            params.append('age', 'old')

            const config = {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }

            axios.post(url, params, config)
                .then((result) => {
                    setGoalItem(result.data.result.slice(0,4));
                    setLocationItem(result.data.result[4].last);
                    console.log(result.data.result[4].last);

                })
                .catch((err) => {
                    console.log(err)

                })
        }
    }, [destinationCors, sourceCors]);
    console.log(sourceCors)
    console.log(destinationCors)


    return (
        <>

            <div className='viewContainer'>
                <div className='flex0'>
                    <Maps sourceRef={sourceRef} destinationRef={destinationRef} directionsRes={directionsRes} />
                    <div className='outputContainer' style={{ color: "white" }}>

                            <input type="submit" onClick={handleSubmit} />
                        <div className='itineries'>
                            <div className='iterItems'>
                            {goalItem.map(goal => {
                                return <div className='goalItems'>
                                    <h4>{goal.name}</h4>
                                    <p>Complete this by this time.
                                        </p>
                                </div>
                            })}
                            {/* </div>
                            {/* <div>
                                {goalItem.map(goal => {
                                return <div className='goalItems'>
                                    <h4>{goal[4].map(g => {
                                        return <div className='goalItems'>
                                                <h4>{goal.name}</h4>
                                        </div>
                                    })}</h4>
                                    <p>Complete this by this time.
                                        </p>
                                </div>
                            })} */}
                            </div> 
                           
                            <div className='iterItems'>
                            {locationItem.map(lt => {
                                return <div className='goalItems'><h4>{lt.name}</h4>
                                <p>
                                <div>{lt.location.lat}   {lt.location.lng}</div>
                                <div>Rating : {lt.rating}</div></p>
                                </div>
                            })}</div>
                            
                               
                                    {/* <div className='goalItems'>
                                        <h4>
                                            Task Title
                                        </h4>
                                        <p>
                                            Complete this by this time.
                                        </p>
                                    </div>
                                    <div className='goalItems'>
                                        <h4>
                                            Task Title
                                        </h4>
                                        <p>
                                            Complete this by this time.
                                        </p>
                                    </div>
                                    <div className='goalItems'>
                                        <h4>
                                            Task Title
                                        </h4>
                                        <p>
                                            Complete this by this time.
                                        </p>
                                    </div> */}
                                    {/* <div className='goalItems'>
                                        <h4>
                                            Task Title
                                        </h4>
                                        <p>
                                            Complete this by this time.
                                        </p>
                                    </div> */}
                                {/* </div> */}
                        </div>
                    </div>
                </div>


                {/* <div className="App">
      <div>
        <div className="search">
          <span><Search /></span>
          <input ref={searchInput} type="text" placeholder="Search location...."/>
          <button onClick={findMyLocation}><GpsFixed /></button>
        </div>
        <div className="address">
          <p>City: <span>{address.city}</span></p>
          <p>State: <span>{address.state}</span></p>
          <p>Zip: <span>{address.zip}</span></p>
          <p>Country: <span>{address.country}</span></p>
        </div>
      </div>
    </div> */}
                <NavBar />


            </div></>
    );
}

//export default Rewards