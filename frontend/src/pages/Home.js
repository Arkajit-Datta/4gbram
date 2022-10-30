import React from 'react'
import './../style/Commentary.css'
import NavBar from './NavBar'
import Homee from './../images/home.jpg'

const Home = () => {
  return (
    <>
        <div className='viewContainer'>
            <img src={Homee} style={{width:'100%', height:'95%', margin:'0% auto 1%'}}></img>
            <NavBar />
        </div>
    </>
  )
}

export default Home