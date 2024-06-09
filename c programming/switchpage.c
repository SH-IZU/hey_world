#include <stdio.h>


int main() {

    char ch;

    printf("Enter a character (a, e, or m): ");

    scanf(" %c", &ch);


    switch (ch) {

        case 'a':

            printf("Good Afternoon\n");

            break;

        case 'e':

            printf("Good Evening\n");

            break;

        case 'm':

            printf("Good Morning\n");

            break;

        default:

            printf("Invalid input\n");

    }

    return 0;

}