import React, { useState, useEffect } from 'react';

function TimeDisplay() {
    const [time, setTime] = useState(new Date().toLocaleTimeString());
    const [randomNum, setRandomNum] = useState(Math.floor(Math.random() * 100)); //1 and 100 are the inclusive lower and upper bound

    useEffect(() => {
        const timer = setInterval(() => {
            setTime(new Date().toLocaleTimeString());
            setRandomNum(Math.floor(Math.random() * 100));
        }, 1000);
        
        // this will clear the interval when the component is unmounted or re-rendered
        return function cleanup() {
            clearInterval(timer);
        }
    }, []);
    
    return (
        <div>
            <h1>Current Time</h1>
            <p>{time}</p>
            <h2>Random Number</h2>
            <p>{randomNum}</p>
        </div>
    );
}

export default TimeDisplay;
