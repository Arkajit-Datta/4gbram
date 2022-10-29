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
                <Link to="/commentary">
                    <div className="navbarItem">
                    {/* <img src={Location} alt="" /> */}
                    Commentary
                    </div>
                </Link>
                <Link to="/rewards">
                    <div className="navbarItem">
                    {/* <img src={Music} alt="" /> */}
                    Map
                    </div>
                </Link>
                <Link to="/profile">
                    <div className="navbarItem">
                    {/* <img src={Emotion} alt="" /> */}
                    Profile
                    </div>
                </Link>
                {/* <Link to="/random">
                    <div className="navbarItem">
                  
                    Random
                    </div>
                </Link> */}
            </div>
        </div>
    </>
  )
}

export default NavBar