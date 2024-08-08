#include <stdio.h>
void printAge(int *pAge){
    printf("You are %d years old.", *pAge);
}
int main(){
    // Pointer = A "variable-like" reference that holds a memory address to another variable, array, etc.
            //   Some tasks are performed more easily with pointers.
            //   * = indirection operator (value at address)

    int age = 21;
    int *pAge = NULL; //good practise to assign NULL if declaring a Pointer.
    pAge = &age;

    printf("Address of age: %p\n", &age);
    printf("Value of pAge : %p\n", pAge);

    printf("Size of age: %d bytes\n", sizeof(age));
    printf("Size of pAge: %d bytes\n", sizeof(pAge));

    printf("Value of age : %d\n", age);
    printf("Value at Stored address : %d\n", *pAge); //dereferencing

    printAge(pAge);
    return 0;
}