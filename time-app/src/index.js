const randomNumber2 = Math.random();
import React from 'react';

import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
console.log(`Random Number 2: ${randomNumber2}`);
