#include <stdio.h>

int main() {
  #ifdef __APPLE__
      printf("Я на macOS\n");
  #elif defined(_WIN32)
      printf("Я на Шindows\n");
    #endif

    return 0;
}
