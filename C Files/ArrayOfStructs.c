#include <stdio.h>
#include <string.h>
// typedef char user[25];
struct Student
{
    char name[25];
    float gpa;
};

int main()
{
    struct Student student1 = {"Spongebob", 3.0}; 
    struct Student student2 = {"Patric", 2.5}; 
    struct Student student3 = {"Sandy", 4.0}; 
    struct Student student4 = {"Squidward", 2.0}; 

    struct Student students[] = {student1, student2, student3, student4};

    for(int i = 0; i <sizeof(students)/sizeof(students[0]); i++){
        printf("%12s\t", students[i].name);
        printf("%.2f\n", students[i].gpa);
    }

    return 0;
}