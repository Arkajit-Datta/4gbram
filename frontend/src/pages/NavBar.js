import React from 'react'

import { Link } from "react-router-dom";
import './../style/NavBar.css'
import Route from './../images/route.png'
import Home from './../images/home.png'
import User from './../images/user.png'
import Mic from './../images/mic.png'

const NavBar = () => {
  return (
    <>
        <div className='navContainer'>
            <div className='items'>
                <Link to="/">
                    <div className="navbarItem">
                    <img src={Home} alt="" />
                    
                    </div>
                </Link>
                <Link to="/commentary">
                    <div className="navbarItem">
                    <img src={Mic} alt="" />
                    </div>
                </Link>
                <Link to="/navigation">
                    <div className="navbarItem">
                    <img src={Route} alt="" />
                    </div>
                </Link>
                <Link to="/profile">
                    <div className="navbarItem">
                    <img src={User} alt="" />
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