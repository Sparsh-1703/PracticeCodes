#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    const int MIN = 1;
    const int MAX = 100;
    int guess;
    int guesses = 0;
    int answer;

    srand(time(0)); // uses cuurent time as a seed to generate random numbers.

    answer = (rand() % MAX) + MIN; // generate a random number between MIN and MAX.
    do
    {
        printf("Enter a guess: ");
        scanf("%d", &guess);
        guesses++;
        if (guess > answer)
        {
            printf("TOO HIGH!!\n");
        }
        else if (guess < answer)
        {
            printf("TOO LOW!!\n");
        }
        else
        {
            printf("CORRECT!!\n");
        }
        
    } while (guess != answer);

    printf("************************\n");
    printf("Answer: %d\n", answer);
    printf("number of Guesses: %d\n", guesses);

    return 0;
}