#include <stdio.h>

int main() {
  int N, i, sum;
  scanf("%d", &N);
  sum=0;
  for(i=1;1;i++) {
    sum+=(2*i-1)*(2*i-1);
    if(sum>N) break;
  }
  printf("%d\n", i-1);
  return 0;
}
