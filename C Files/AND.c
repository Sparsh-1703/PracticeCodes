#include <stdio.h>
#include <stdbool.h>
int main(){
    //Logical Operator = && (AND) checks if two or more conditions are true.
    float temp = 25;
    bool sunny = false;
    if(temp>= 0 && temp <=30 && sunny){ //(sunny == true)
        printf("\nThe Weather is good!");
    }
    else{
        printf("\nThe Weather is bad!");
    }
}