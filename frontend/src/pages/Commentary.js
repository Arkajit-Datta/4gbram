import React, { useEffect } from 'react'
import './../style/Commentary.css'
import NavBar from './NavBar'
import audioImg from './../images/audio1.png'
import { useHistory } from "react-router-dom";

import axios from 'axios';

// import audio1 from "../assets/audio1.mp3"
// import ibm from "../../public/TTSAudios/ibmTTs.mp3"
// import ind from "../../public/TTSAudios/indTTS.mp3"


const Commentary = ({ location }) => {
  if (!location.state) history.push('/commentary')
  const history = useHistory();

  let audioPlayer = new Audio("../assets/audio1.mp3");

  React.useEffect(()=>{
    return function cleanup () {
      clearInterval(timer)
    }
  })

  
  const changePage = () => {
    history.push('/commentary')
  }


  const timer=setInterval(() => {
    axios.get('http://localhost:5000/audio').then((res) => {
      console.log(res.data);
      audioPlayer.src="../assets"+res.data[0].path
      document.getElementById('audioButton').click();
    })

  }, 3000);

  const [mood, setMood] = React.useState(location.state.type);
  console.log(mood)
  const getSelectedMode = () => {
    switch (mood) {
      case 'nice':
        return <>Be Nice</>
      case 'roast':
        return <>Roast me</>
      case 'educate':
        return <>Educate me</>
      default:
        break;
    }
  }
  return (
    <>
      <div className='viewContainer'>
      {/* <audio id="player" autoPlay controls><source src="audio1.mp3" type="audio/mp3"/></audio> */}
        <div className='options'>
          <div className='cancelOption' onClick={changePage}>
            Back
          </div>
          <div className='mode'>
            Selected Mode: {getSelectedMode()}
          </div>
        </div>
        <div className='options1'>
          <div className='mode' onClick={()=>audioPlayer.play()} id='audioButton'>
            Cancel Commentary
          </div>
        </div>
        <div className='audioAnimation'>
          <img src={audioImg}></img>
        </div>
        <div className='suggestions'>
          <h1>Vehicle Status</h1>
          <h2>Best practice</h2>
        </div>
        <NavBar />
      </div>

    </>
  )
}

export default Commentary