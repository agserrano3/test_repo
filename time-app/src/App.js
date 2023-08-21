import React from 'react';
import './App.css';
import TimeDisplay from './TimeDisplay';
import JokeButton from './JokeButton';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <TimeDisplay />
        <JokeButton />
      </header>
    </div>
  );
}

export default App;  
