import React from 'react'
import './../style/Commentary.css'
import NavBar from './NavBar'
import Audio from './../images/audio1.png'

const Commentary = () => {
  return (
    <>
        <div className='viewContainer'>
            <div className='options'>
              <div className='cancelOption'>
                Back
              </div>
              <div className='mode'>
                Selected Mode: Be Nice
              </div>
            </div>
            <div className='audioAnimation'>
              <img src={Audio}></img>
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