import React, { useState, useEffect } from 'react';

function TimeDisplay() {
    const [time, setTime] = useState(new Date().toLocaleTimeString());
    
    const random_number3 = Math.floor(Math.random() * 100) + 1;
    console.log(`Random number 3: ${random_number3}`);

    useEffect(() => {
        const timer = setInterval(() => setTime(new Date().toLocaleTimeString()), 1000);

        // this will clear the interval when the component is unmounted or re-rendered
        return function cleanup() {
            clearInterval(timer);
        }
    }, []);
    
    return (
        <div>
            <h1>Current Time</h1>
            <p>{time}</p>
        </div>
    );
}

export default TimeDisplay;