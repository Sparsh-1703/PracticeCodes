#include <stdio.h>
int main(){
    //nested loop = a loop within another loop.
    int rows;
    int columns;
    char symbol;

    printf("Enter number of Rows: ");
    scanf("%d", &rows);

    printf("Enter number of Columns: ");
    scanf("%d", &columns);

    scanf("%c");

    printf("Enter a symbol to use: ");
    scanf("%c", &symbol);   
    
    for(int i = 1; i<=rows; i++){
        for(int j = 1; j <= columns; j++){
            printf("%c", symbol);
    }
        printf("\n");
    }
    return 0;
}