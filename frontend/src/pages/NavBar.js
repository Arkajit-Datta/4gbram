import React from 'react'

import { Link } from "react-router-dom";
import './../style/NavBar.css'


const NavBar = () => {
  return (
    <>
        <div className='navContainer'>
            <div className='items'>
                <Link to="/">
                    <div className="navbarItem">
                    {/* <img src={Home} alt="" /> */}
                    Home
                    </div>
                </Link>
                <Link to="/location">
                    <div className="navbarItem">
                    {/* <img src={Location} alt="" /> */}
                    Location
                    </div>
                </Link>
                <Link to="/video">
                    <div className="navbarItem">
                    {/* <img src={Music} alt="" /> */}
                    Music
                    </div>
                </Link>
                <Link to="/emotion">
                    <div className="navbarItem">
                    {/* <img src={Emotion} alt="" /> */}
                    Emotion
                    </div>
                </Link>
                <Link to="/random">
                    <div className="navbarItem">
                    {/* <img src={Random} alt="" /> */}
                    Random
                    </div>
                </Link>
            </div>
        </div>
    </>
  )
}

export default NavBar