const randomNumber1 = Math.random();
import React from 'react';

import './App.css';
import TimeDisplay from './TimeDisplay';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <TimeDisplay />
      </header>
    </div>
  );
}

console.log(`Random Number 1: ${randomNumber1}`);
export default App;
