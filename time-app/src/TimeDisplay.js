import React, { useState, useEffect } from 'react';

function TimeDisplay(props) {
    let format = props.format ? props.format : '';
    const [time, setTime] = useState(new Date().toLocaleTimeString('default', {timeStyle: format}));

    useEffect(() => {
        const timer = setInterval(() => setTime(new Date().toLocaleTimeString('default', {timeStyle: format})), 1000);

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