import React from 'react'
import NavBar from './NavBar'
import './../style/Profile.css'
import { useHistory } from "react-router-dom";
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
                        <h3>a</h3>
                    </div>
                    <div className='mainContentItem2'>
                        <div className='mainItem'>
                        <h3>a</h3>
                        </div>
                        <div className='mainItem'>
                        <h3>Badge</h3>
                        </div>
                        <div className='mainItem'>
                        <h3>K.D.</h3>
                        </div>
                        <div className='mainItem'>
                        <h3>a</h3>
                        </div>
                    </div>
                </div>
                <div className='communityRelated'>
                    {/*  */}
                    <div className='communityCard' onClick={() => changePage("/profile/mystats")}>
                        <h3>My Stats</h3>
                        <p>Lorem ipsum dolor sit amet.</p>
                    </div>
                    <div className='communityCard' onClick={() => changePage("/profile/currentstandings")}>
                        <h3>Current Standings</h3>
                        <p>Lorem ipsum dolor sit amet.</p>

                    </div>
                    
                </div>
            </div>
            
            <NavBar />
        </div>
    </>
  )
}

export default Profile