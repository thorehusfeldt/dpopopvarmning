#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> barn;
int n,v[100],h[100],langd[100];

int ok() {   //Kontrollerar om den permutation som för tillfället ligger i barn[0..n-1] stämmer med indatan
  int i,j,rv,rh;
  for(i=0;i<n;i++) {
    rv=rh=0;
    for(j=0;j<i;j++) if(langd[barn[j]] > langd[barn[i]]) rv++; //Räkna antalet längre barn till vänster om barn[i]
    for(j=i+1;j<n;j++) if(langd[barn[j]] > langd[barn[i]]) rh++;  //Räkna antalet längre barn till höger om barn[i]
    if(rv!=v[barn[i]] || rh!=h[barn[i]]) return 0; //Returnera 0 om det inte stämmer med indatan
  }
  return 1;
}

int main() {
  int i;
  cin >> n;
  for(i=0;i<n;i++){
    cin >> v[i];
    cin >> h[i];
    langd[i]=n-v[i]-h[i]; //Ge barnet en relativ längd
  }
  for(i=0;i<n;i++) barn.push_back(i); //Starta med permutationen [0,1,2,3...n-1]
  do {
    if(ok()) {
      for(i=0;i<n;i++) cout << (char)(barn[i]+'A');
      cout << endl;
      return 0;
    }
  } while (next_permutation(barn.begin(),barn.end()));
  return 1; //Här skulle vi hamna om något barn givit en felaktig uppgift
}
