#include <stdio.h>
int main(){
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);
    
    if (age>=18){
        printf("You are now signed up!!");
    }
    else if(age ==0){
        printf("Ain't no way blud.");
    }
    else if(age <0){
        printf("Nice try bud ;)");
    }
    else{
        printf("You are too young to sign up!");
    }
}