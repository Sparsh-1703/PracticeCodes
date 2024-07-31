#include <stdio.h>
#include <ctype.h>
int main(){
    char unit;
    float temp;

    printf("Is the Temperature in (F) or (C)?: ");
    scanf("%c", &unit);

    unit = toupper(unit);

    if(unit == 'C'){
        printf("\nEnter the Temperature in Celcius: ");
        scanf("%f", &temp);
        temp = (temp*9/5) + 32;
        printf("\nThe Temperature in Farenheit is: %.1lf F", temp);
    }
    else if (unit == 'F'){
        printf("Enter the Temperature in Farenheit: ");
        scanf("%f", &temp);
        temp  = ((temp -32)*5)/9;
        printf("\nThe Temperature in Celcius is: %.1lf C", temp);
    }
    else{
        printf("\n %c is not a valid user of measurement!", unit);
    }
    return 0;
}