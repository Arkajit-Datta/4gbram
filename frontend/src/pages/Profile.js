import React from 'react'
import NavBar from './NavBar'
import './../style/Profile.css'
import { useHistory } from "react-router-dom";
import './../style/Commentary.css'
import Badge from './../images/medal.png'
import Goal from './../images/goal.png'
import Rating from './../images/rating.png'
import Coupons from './../images/coupons.png'
import Graph from './../images/graph.png'
import Podium from './../images/podium.png'

const Profile = () => {
    const history = useHistory();
    function changePage(s){
        history.push(s);
    }
  return (
    <>
        <div className='viewContainer'>
            <div className='bigContainer'>
                <div className='mainContent'>
                    <div className='mainContentItem1'>
                        <h3>Name: Arkajit Datta</h3><br></br>
                        <h3>Car-Model: JEEP</h3><br></br>
                        <h3>Chasis No: 82734A3423</h3><br></br>
                        <h3>Number plate: TS 09 HS0232</h3><br></br>
                    </div>
                    <div className='mainContentItem2'>
                        <div className='mainItem'>
                        <img src={Badge}></img><h3>Badge</h3>
                        Silver
                        </div>
                        <div className='mainItem'><img src={Goal}></img>
                        <h3>Recent Accomplishments</h3>

                        </div>
                        <div className='mainItem'><img src={Rating}></img>
                        <h3>Overall Rating</h3>
                        7.6
                        </div>
                        <div className='mainItem'><img src={Coupons}></img>
                        <h3>Redeem My Coupons</h3>
                        13 Coupons available
                        </div>
                    </div>
                </div>
                <div className='communityRelated'>
                    {/*  */}
                    <div className='communityCard' onClick={() => changePage("/profile/mystats")}>
                    <img src={Graph}></img><h3>My Stats</h3>
                        <p>Current Rating: 7.0</p>
                    </div>
                    <div className='communityCard' onClick={() => changePage("/profile/currentstandings")}>
                    <img src={Podium}></img><h3>Current Standings</h3>
                        <p>Current Rank: 54</p>

                    </div>
                    
                </div>
            </div>
            
        
            <NavBar />
        </div>
        
    </>
  )
}

export default Profile