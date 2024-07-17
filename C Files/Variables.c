#include <stdio.h>
int main(){
//     Variable = Allocated Space in memory to sotre a value.
//                We refer to variable's name to access the stored value.
//                That variable now behaves as if it was the value it contains.
//                BUT we have to DECLARE what TYPE OF DATA we are storing.
    int x; //declaration
    x = 123; //initializaion 
    int y = 321; //declaration + initialization 

    int age = 19; //integer 
    float gpa = 2.05; //floating point number 
    char grade = 'C'; // single character
    char name[] = "Bro"; //array of characters
    
    printf("Hello %s!\n", name);
    printf("You are %d years old.\n", age);
    printf("Your average grade is %c.\n", grade);
    printf("Your gpa is %f\n", gpa);
    return 0;
}