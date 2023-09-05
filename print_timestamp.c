#include <time.h>   // Include the time library
#include <stdio.h>  // Include the standard I/O library

int main() {
    time_t current_time; // Declare a variable to hold the time
    current_time = time(NULL); // Get the current time
    
    if (current_time == ((time_t)-1)) {
    fprintf(stderr, "Failure to compute the current time.");
    return 1;
    }
    
    char *timestamp = ctime(&current_time); // Format the time to a string
    if (timestamp == NULL) {
    fprintf(stderr, "Failure to convert the current time.");
    return 1;
    }
    
    printf("Current time: %s", timestamp); // Print the formatted time
    return 0;
}
