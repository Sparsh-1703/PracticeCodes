#include <stdio.h>
#include <stdbool.h>
int main(){
    //Logical Operators = !! (OR) checks if at least one of the conditions is true.
    float temp = 25;
    if(temp <= 0 || temp >= 30){
        printf("The Temperature is bad!");
    }
    else{
        printf("The Temperature is good.");
    }
    return 0;
}