#include <stdio.h>

int main(){
  int na,nb,sa,sb,a[10],b[10],i;
  scanf("%d",&na);
  scanf("%d",&nb);
  sa=0;
  for(i=0;i<na;i++) {
    scanf("%d",&a[i]);
    sa+=a[i];
  }
  sb=0;
  for(i=0;i<nb;i++) {
    scanf("%d",&b[i]);
    sb+=b[i];
  }

  for(i=0;i<na;i++) if(a[i]*na<sa && a[i]*nb>sb) { //Om a[i] < sa/na och a[i] > sb/nb
    printf("%d B\n",a[i]);
    return 0;
  }
  for(i=0;i<nb;i++) if(b[i]*nb<sb && b[i]*na>sa) { //Om b[i] < sb/nb och a[i] > sa/na
    printf("%d A\n",b[i]);
    return 0;
  }
  printf ("NEJ\n");
  return 0;
}
