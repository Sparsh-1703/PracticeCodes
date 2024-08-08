#include <stdio.h>
int main(){

    FILE *pF = fopen("test.txt", "a");

    fprintf(pF, "\nSpongebob Squarepants");

    fclose(pF);

  /*  if(remove("text.txt") == 0){
        printf("File was deleted successfully!");
    }
    else{
        printf("File was NOT deleted.");
    }  */

     return 0;
}