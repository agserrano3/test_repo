import React from 'react';
import './App.css';
import TimeDisplay from './TimeDisplay';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <TimeDisplay format="short" />
      </header>
    </div>
  );
}

export default App;