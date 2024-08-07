#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
    // pseudo random numbers = A set of values or elements that are statistically random
    //                         (DON'T USE for any cryptograhic SECURITY!!)
    srand(time(0));

    int number1 = (rand() % 6) + 1;
    int number2 = (rand() % 6) + 1;
    int number3 = (rand() % 6) + 1;
    printf("%d\n", number1);
    printf("%d\n", number2);
    printf("%d\n", number3);
    
    return 0;
}