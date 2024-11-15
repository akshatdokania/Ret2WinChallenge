#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Function to generate the secret password
void generate_password(char *password, int length) {
    srand(1337);
    for (int i = 0; i < length; i++) {
        password[i] = (rand() % 26) + 'A';
    }
    password[length] = '\0';
}

void bomb_explodes() {
    printf("\n💥 BOOM! The bomb exploded! 💥\n");
    exit(1);
}

void bomb_defused() {
    printf("\n🎉 Congratulations! You defused the bomb! 🎉\n");
    exit(0);
}

int main() {
    const int password_length = 8;
    char secret_password[password_length + 1];
    char input[128];

    generate_password(secret_password, password_length);

    printf("The bomb is armed! To defuse it, you must enter the correct password.\n");
    printf("Enter the password: ");
    fflush(stdout);

    if (fgets(input, sizeof(input), stdin) == NULL) {
        bomb_explodes();
    }
    
    input[strcspn(input, "\n")] = 0;

    if (strcmp(input, secret_password) == 0) {
        bomb_defused();
    } else {
        bomb_explodes();
    }

    return 0;
}