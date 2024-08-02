#include <stdio.h>
int main(){
    // Array = a data structure that can store many values of the same data type.
    double prices[5]= {5.0, 10.5 , 15, 20, 25.8};
    printf("$%.2lf\n", prices[0]);
    for(int i = 0; i <5; i++){
    // for(int i = 0; i <sizeof(prices)/sizeof(prices[0]); i++)
        printf("$%.2lf\n", prices[i]);
    }
    return 0;
}