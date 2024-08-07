#include <stdio.h>
int main(){
    //BITWISE OPERATOS = special operators used in bit-level programming.

    // & = AND               like AND Gate
    // ! = OR                like OR Gate
    // ^ = XOR               like XOR Gate(If only one is 1, then only 1)
    // << = LEFT shift       shifts bits to the left
    // >> = RIGHT shift      shifts bits to the right

    int x = 6;     //6  = 00000110
    int y = 12;    //12 = 00001100
    int z = 0;     //0  = 00000000
    
    z = x & y;
    printf("AND = %d\n", z);
    z = x | y;
    printf("OR = %d\n", z);
    z = x ^ y;
    printf("XOR = %d\n", z);
    z = x << 1;
    printf("SHIFT LEFT = %d\n", z);
    z = x >> 1;
    printf("SHIFT RIGHT = %d\n", z);

    return 0;
}