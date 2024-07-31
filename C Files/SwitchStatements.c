#include <stdio.h>
int main()
{
    // Switch statement = A more efficient alternative to using many "else-if" statements
    //                    allows a value to be tested for equality against many cases.
    char grade;
    printf("Enter a letter grade: ");
    scanf("%c", &grade);

    switch (grade)
    {
    case 'A':
        printf("perfect!\n");
        break;
    case 'B':
        printf("You did good!\n");
        break;
    case 'C':
        printf("You did okay.\n");
        break;
    case 'D':
        printf("At lease its not a F.\n");
        break;
    case 'F':
        printf("You failed..");
        break;
    default:
        printf("Please enter Valid grades!!");
    }
}