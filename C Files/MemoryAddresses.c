#include <stdio.h>
int main(){
    // memory = an array of bytes within RAM (like a street)
    // memory block = a single unit (byte) within memory, used to hold some value (a person)
    // memory address = the address of where a memory block is located (house address)

    char a;
    double b[3];

    printf("%d bytes\n", sizeof(a));
    printf("%d bytes\n", sizeof(b));

    printf("%p\n", &a);
    printf("%p\n", &b);
    
    return 0;
}