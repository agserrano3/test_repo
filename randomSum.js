function randomSum() {
    // generate two random numbers 
    var num1 = Math.random();
    var num2 = Math.random();

    // log the numbers to the console
    console.log("Random Numbers: ", num1, num2);
    

    // return the sum of the two numbers
    return num1 + num2;
}

// call the function and print the result to the console
console.log('Sum of Two Random Numbers: ', randomSum());
