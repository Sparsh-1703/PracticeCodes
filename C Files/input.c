#include <stdio.h>
int main(){
    char name[25]; //bytes
    int age;
    printf("What is your name? ");
    scanf("%s", &name);
    printf("Hello %s, how are you? ", name);

    printf("\nHow old are you? ");
    scanf("%d", &age);
    printf("You are %d years old." , age);
    return 0;
}