#include <stdio.h>
#include <stdlib.h>
#include<time.h>
void delay(unsigned int mseconds)
{
    clock_t goal = mseconds + clock();
    while (goal > clock());
}
int main(int argc, char *argv[])
{
  if (argc < 3) {
    printf("Error: Improper parameter!\n");
    return 0;
  }

  long long int start, end;
  start = atoll(argv[1]);
  end = atoll(argv[2]);

  //  printf("start = %i, end = %i\n", start, end);
  for (int i = start; i <= end; i++) {
    printf("%i\n", i);
    delay(1000000);
  }

  return 0;
}
