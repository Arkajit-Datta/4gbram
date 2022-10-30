import React, { useState } from 'react'
import NavBar from './NavBar'
import '../../node_modules/react-vis/dist/style.css';
import Statss from './../images/stats.jpg'

function Stats() {
  return (
    <>
        <div className='viewContainer'>
        <img src={Statss} style={{width:'100%', height:'95%', margin:'0% auto 1%'}}></img>
            <NavBar />
        </div>
    </>
  )
}

export default Stats

