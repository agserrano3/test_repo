import React from 'react';

// Array of jokes
const jokes = [
  "Why don't scientists trust atoms? Because they make up everything!",
  "Why did the scarecrow win an award? Because he was outstanding in his field!",
  "Why don't some animals play cards? Because they are afraid of cheetahs!"
];
  
function JokeButton() {
  // Function to handle button click and display a random joke
  function handleJoke() {
    const joke = jokes[Math.floor(Math.random() * jokes.length)];
    alert(joke);
  }

  return (
    <button onClick={handleJoke}>
      Tell me a joke!
    </button>
  );
}
  
export default JokeButton;
