import React, { useState, useEffect } from 'react';

function RandomNumberDisplay() {
    const [randomNum, setRandomNum] = useState(Math.floor(Math.random() * 100)); //1 and 100 are the inclusive lower and upper bound

    useEffect(() => {
        const timer = setInterval(() => setRandomNum(Math.floor(Math.random() * 100)), 1000);

        return function cleanup() {
            clearInterval(timer);
        }
    }, []);
    
    return (
        <div>
            <h2>Random Number</h2>
            <p>{randomNum}</p>
        </div>
    );
}

export default RandomNumberDisplay;
