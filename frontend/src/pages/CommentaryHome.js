import React from 'react'
import './../style/Commentary.css'
import NavBar from './NavBar'
import Audio from './../images/audio1.png'
import { useHistory } from "react-router-dom";

const CommentaryHome = () => {
    const history = useHistory();
    const changePage = (type) => {
      history.push('/commentary/play',{ type:type })
    }
  return (
    <>
        <div className='viewContainer'>
            <div className='options'>
                <h1>Select A Mode</h1>
            </div>
            <div className='selectModes'>
              <div className='availableOption' onClick={()=>changePage('nice')}>
                Be Nice
              </div>
              <div className='availableOption' onClick={()=>changePage('roast')}>
                Roast Me
              </div>
              <div className='availableOption' onClick={()=>changePage('educate')}>
                Educate Me
              </div>
            </div>
            <NavBar />
        </div>
  
    </>
  )
}

export default CommentaryHome