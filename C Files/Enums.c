#include <stdio.h>

enum Day{Sun = 1, Mon = 2, Tue = 3, Wed = 4, Thu = 5, Fri = 6, Sat = 7};
int main(){
    // enum = a user defined type of names integer identifiers
    //        helps to make a program more readable.
    enum Day today = Sun;
    printf("%d\n", today); //enums are NOT STRINGS, but they can be treated as int
    if(today == Sun || today == Sat){
        printf("Its Weekend!!");
    }
    else{
        printf("Work day :(");
    }
    return 0;
}