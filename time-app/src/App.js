import React from 'react';
import './App.css';
import TimeDisplay from './TimeDisplay';
import RandomNumberDisplay from './RandomNumberDisplay';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <TimeDisplay />
        <RandomNumberDisplay />
      </header>
    </div>
  );
}

export default App;

