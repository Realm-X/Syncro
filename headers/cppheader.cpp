#include <pybind11/pybind11.h>
#include <cstdlib>

namespace py = pybind11;
bool isConnected() 
{
  
    int response = system("ping -n 1 8.8.8.8 > nul");
    return (response == 0);
}

PYBIND11_MODULE(network_utils, m) 
{
    m.doc() = "A module to check internet connectivity";
    m.def("is_connected", &isConnected, "Check if the internet is connected");
}
