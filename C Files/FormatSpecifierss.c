#include <stdio.h>
int main (){
    // format specifiers % = defines and formats a type of data to be displayed

    // %c  = character 
    // %s  = string (array of characters)
    // %f  = float
    // %lf = long float
    // %d  = integer

    // %.1 = decimal precision
    // %1 = minimum field width
    // %- = left margin

    float item1 = 5.75;
    float item2 = 10.00;
    float item3 = 100.99;

    printf("Item 1: $%0.2f\n", item1);
    printf("Item 2: $%8.2f\n", item2);
    printf("Item 3: $%-8.2f\n", item3);
    return 0;
}