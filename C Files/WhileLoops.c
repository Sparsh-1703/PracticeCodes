#include <stdio.h>
#include <string.h>
int main(){
    // while loop = returns section of code possibly unlimited times.
    // WHILE some conditions remain true.
    // a While loop might not execute at all.
    char name[25];

    printf("What is your name? ");
    fgets(name, 25, stdin);
    name[strlen(name)-1] = '\0';

    while(strlen(name) == 0){
        printf("you didn't enter your name!!!");
        printf("\nWhat is your name? ");
        fgets(name, 25, stdin);
        name[strlen(name)-1] = '\0';
    }
    printf("Heyy %s!!", name);
    return 0;   
}