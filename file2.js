const fs = require('fs');
const randomNumber = Math.random();
fs.writeFile('randomNumber2.txt', randomNumber.toString(), (err) => {
    if (err) throw err;
    console.log('RANDOM NUMBER WRITTEN TO RANDOMNUMBER2.TXT');
});