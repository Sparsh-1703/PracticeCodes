#include <stdio.h>
#include <string.h>
int main(){
    char string1[] = "Sigma";
    char string2[] = "Male";

    strlwr(string1);                                   // converts a string to lowercase       
    strupr(string1);                                   // converts a string to UPPERCASE 
    strcat(string1, string2);                          // appends string2 to the end of string 1
    strncat(string1, string2, 1);                      // appends n characters from string2 to string1
    strcpy(string1, string2);                          // copy string2 to string1 (replace)
    strncpy(string1, string2, 2);                      // copy n characters of string2 to string1 (replace)

    strset(string1, '?');                              // sets all characters of a string to a given character
    strnset(string1, 'x', 1);                          // sets first n characters of a string to a given character
    strrev(string1);                                   // reverses a string

    int result = strlen(string1);                      // returns lenght of string as an Integer
    int result = strcmp(string1, string2);             // string compare all characters
    int result = strncmp(string1, string2, 1);         // string compare n characters
    int result = strcmpi(string1, string1);            // string compare all characters (ignore Case Sensitivity)
    int result = strnicmp(string1, string2, 1);        // string compare n characters (ignore Case Sensitivity)
    printf("%d", result);
}