const fs = require('fs');
const randomNumber = Math.random();
fs.writeFile('randomNumber1.txt', randomNumber.toString(), (err) => {
    if (err) throw err;
    console.log('Random number written to randomNumber1.txt');
});