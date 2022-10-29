import React, { useRef, useState } from 'react'

import NavBar from './NavBar';
import './../style/Location.css'
//import { Search, GpsFixed } from "@material-ui/icons"
//import './../style/Home.css'
import { useEffect } from "react";

//import Iternary from '../comps/Iternary';
//import Recommends from '../comps/Recommends';
import Maps from '../pages/comps/Map.js';
import { geocodeByAddress } from "react-places-autocomplete";
import axios from 'axios';
import { useHistory } from "react-router-dom";

import qs from 'qs';

const directionsService = new window.google.maps.DirectionsService;

// const url = 'http://localhost:5000/gen_video'
export default function Rewards() {

    const [sourceCors, setSource] = useState({ lat: '', lon: '' });
    const [destinationCors, setDestination] = useState({ lat: '', lon: '' });
    const [directionsRes, setdirectionsRes] = useState();
    const [selectedEmotion, setselectedEmotion] = useState('happy');
    const [video, setVideo] = useState();
    const sourceRef = useRef();
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

        //API CALLING CODE INSERT BELOW
        //SOURCECORS AND DESTINATION CORS CONRTAIN THE LAT AND LONG COordinates


        // apiCall({ body: body })
    }


    async function getDirections({ source, destination }) {
        const res = await directionsService.route({
            origin: source,
            destination: destination,
            travelMode: window.google.maps.TravelMode.DRIVING
        })
        setdirectionsRes(res);
    }
    useEffect(() => {
        if (destinationCors.lat != '' && sourceCors.lat != '') {
            const params = new URLSearchParams()
            params.append('slat', sourceCors.lat)
            params.append('slong', sourceCors.lon)
            params.append('dlat', destinationCors.lat)
            params.append('dlong', destinationCors.lon)

            params.append('mood', selectedEmotion)
            params.append('age', 'old')

            const config = {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }

            // xios.post(url, params, config)
            //     .then((result) => {
            //         console.log(result)
            //         setVideo(result.data)
            //         history.push("/video");
            //         localStorage.setItem('videoSrc','/home/anirudh/Desktop/Chaarminar/frontend/public/full_video.mp4')
            //     })
            //     .catch((err) => {
            //         console.log(err)

            //     })
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
                        <div className='filter'>
                            <ul>
                                {/* <li style={{ backgroundColor: selectedEmotion == "happy" ? 'cyan' : '#1e1e34' }} className='moodContainer' onClick={() => setselectedEmotion('happy')}> <img src={Happy}></img>
                                </li>
                                <li style={{ backgroundColor: selectedEmotion == "sad" ? 'cyan' : '#1e1e34' }} className='moodContainer' onClick={() => setselectedEmotion('sad')}>
                                    <img src={Sad} alt=""></img>
                                </li >
                                <li style={{ backgroundColor: selectedEmotion == "angry" ? 'cyan' : '#1e1e34' }} className='moodContainer' onClick={() => setselectedEmotion('angry')}>
                                    <img src={Angry} alt=""></img>
                                </li>
                                <li style={{ backgroundColor: selectedEmotion == "neutral" ? 'cyan' : '#1e1e34' }} className='moodContainer' onClick={() => setselectedEmotion('neutral')}>
                                    <img src={Neutral} alt=""></img></li> */}
                            </ul>
                            <select>
                                <option>One</option>
                                <option>Two</option>
                                <option>Three</option>
                            </select>
                            <input type="submit" onClick={handleSubmit} />
                        </div>
                        <div className='itineries'>
                            {/* <h2>Itineries</h2>
                            <div className='iterItems'>
                                <Iternary />
                                <Iternary />
                                <Iternary />
                            </div>
                            <hr></hr> */}
{/* 
                            <h2>Recomendations</h2>
                            <div className='recommendations'>
                                <Recommends name="Gas Stations" />
                                <Recommends name="Restaurants" />
                                <Recommends name="Music" />
                                <Recommends name="Tourist Spots" />
                                <Recommends name="Music" />
                                <Recommends name="Amusement Parks" />
                            </div> */}
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