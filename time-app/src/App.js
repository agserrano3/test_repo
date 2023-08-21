function renderJoke() {
  const jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why was the math book sad? Because it had too many problems!",
    "Why can't you give Elsa a balloon? Because she will let it go!"
    // ...add as many jokes as you wish in this array.
  ];

  const index = Math.floor(Math.random() * jokes.length);
  const joke = jokes[index];

  alert(joke);
}

import React from 'react';

import './App.css';
import TimeDisplay from './TimeDisplay';

function App() {
  return (
    <div className="App">
      <header className="App-header">
                <TimeDisplay />
        <button onClick={renderJoke}>Click for a joke!</button>
      </header>

    </div>
  );
}

export default App;