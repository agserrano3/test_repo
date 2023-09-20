import React from 'react';
import './App.css';
import TimeDisplay from './TimeDisplay';

function App() {
  const random_number2 = Math.floor(Math.random() * 100) + 1;
  console.log(`Random number 2: ${random_number2}`);
  return (
    <div className="App">
      <header className="App-header">
        <TimeDisplay />
      </header>
    </div>
  );
}

export default App;