#include <iostream>
#include <cstring>
int main() {
    char buf[10];
    gets(buf);  // unsafe
    int x;      // unused
    int* p = new int[10]; // memory leak
    std::cout << buf << std::endl;
    return 0;
}

