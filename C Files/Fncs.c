#include <stdio.h>
void birthday(char name[], int age){
    printf("Happy birthday dear %s!", name);
    printf("\nYou are %d years old as of now!!", age);
}
int main(){
    char name[]= "Sigmeshhh";
    int age = 19;
    birthday(name, age);
    return 0;
}