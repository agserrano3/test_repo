#include <ctime>
#include <iostream>
#include <chrono>

int main() {
    // Include the ctime and chrono libraries in your existing C++ program.
    
    // Before you generate a number, get the current time and store it in a variable.
    auto start_time = std::chrono::system_clock::now();
    
    // Generate a random number
    int random_integer = 1 + (rand() % 10);
    
    // Immediately after this, get the current time again and store it in another variable.
    auto end_time = std::chrono::system_clock::now();
    
    // The difference in these two times is the time taken to generate the random number. You can print this.
    std::chrono::duration<double> elapsed_seconds = end_time - start_time;
    std::time_t end_time_t = std::chrono::system_clock::to_time_t(end_time);
    std::cout << "Time taken to generate a random integer in CPP: " << elapsed_seconds.count() << "s\n";
    
    return 0;
}
