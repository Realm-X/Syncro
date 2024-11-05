#include <iostream>
#include <cstdlib>  // For system()

// Function to check if the user is connected to the Internet
bool isConnected() 
{
    // Ping Google's DNS server (8.8.8.8) - Windows Syntax
    int response = system("ping -n 1 8.8.8.8 > nul");
    return (response == 0);
}

