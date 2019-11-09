#include <stdio.h>

int p[1000];

int hitta(int m, int n) {  //Hittar närmsta gemensamma anfader till m och n.
  int k;
  for(;m>0;m=p[m])   //Gå uppåt från ena personen.
     for(k=n;k>0;k=p[k])    //Gå uppåt från andra personen.
        if(k==m) return k;     //Ta första bästa.
}


int main() {
  int N,M,i,anf,g[1000];
  scanf("%d%d", &N, &M);
  for(i=1;i<=N;i++) scanf("%d", &p[i]);
  for(i=0;i<M;i++) scanf("%d", &g[i]);
  anf=g[0];
  for(i=1;i<M;i++) anf=hitta(anf,g[i]);   //Väljer närmsta gemensamma anfader mellan den hittills hittade och var och en av personerna vid bordet.
  printf("%d\n", anf);
  return 0;
}
