#include <iostream>
namespace first{
    int x = 1; 
}
namespace second{
    int x = 2;
}
int main(){
    std::cout << first::x << std::endl;
    std::cout << second::x << std::endl;
}
// namespace = provides a solution for preventing name conflicts in large projects.
//             each entity needs a unique name. A namespace allows identically named
//             entities as long as the namespace are different.