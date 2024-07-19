#include <stdio.h>
#include <stdbool.h>
int main(){
    char a = 'C';                   // Single Character         %c
    char b[]= "Bro";                // Array of Characters      %s

    float c = 3.141592;             // 4 Bytes (32 bits of precision) 6-7 digits    %f
    double d = 3.141592653589793;   // 8 Bytes (64 bits of precision) 15-16 digits  %lf 

    bool e = true;                  // 1 Byte (True of False)   %d

    char f = 120;                   // 1 Byte (-128 to +127)    %d or %c
    unsigned char g = 256;          // 1 Byte (0 to +255)       %d or %c

    short int h = 32767;            // 2 bytes (-32,768 to +32,767)   %d
    unsigned short int i = 65535;   // 2 bytes (0 to +65,535)         %d

    int j = 2147483647;             // 4 Bytes (-2,147,483,648 to +2,147,483,647)  %d
    unsigned int k = 4294967295L;   // 4 Bytes (0 to +4,294,967,295)               %u

    long long int l = 9223372036854775807;              // 8 Bytes (-9 quintillion + 9 quintillion)  %llu
    unsigned long long int m = 18446744073709551615U;    // 8 Bytes (0 to +18 quintillion)            %lld
}