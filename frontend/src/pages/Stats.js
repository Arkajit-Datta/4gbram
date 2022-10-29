import React, { useState } from 'react'
import NavBar from './NavBar'
import '../../node_modules/react-vis/dist/style.css';
import {XYPlot, LineSeries,Highlight,MarkSeries,VerticalGridLines,HorizontalGridLines,XAxis,YAxis,Crosshair} from 'react-vis';

function Stats() {
    const data = [
        {x: 0, y: 8},
        {x: 1, y: 5},
        {x: 2, y: 4},
        {x: 3, y: 9},
        {x: 4, y: 1},
        {x: 5, y: 7},
        {x: 6, y: 6},
        {x: 7, y: 3},
        {x: 8, y: 2},
        {x: 9, y: 0}
    ]

  return (
    <>
        <div className='viewContainer'>
   
            <NavBar />
        </div>
    </>
  )
}

export default Stats

// onMouseLeave={() => setState({crosshairValues: []})}
//         width={600}
//         height={600}>
//         <VerticalGridLines />
//         <HorizontalGridLines />
//         <XAxis />
//         <YAxis />
//         <LineSeries
//           onNearestX={(value, {index}) =>
//           	setState({crosshairValues: DATA.map(d => d[index])})}
//           data={DATA[0]}/>
//         <LineSeries
//           data={DATA[1]}/>
//         <Crosshair values={state.crosshairValues}/>