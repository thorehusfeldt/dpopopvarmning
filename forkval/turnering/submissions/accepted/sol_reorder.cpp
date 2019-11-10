#include <iostream>
#include <algorithm>
#include <vector>

int main(){
	using namespace std;
	int posses,turns;
	cin >> posses;
	cin >> turns;
	--turns; //Räkning sker från 0, inte 1
	vector<int> vec;
	for(int i=1;i<posses;++i)
		vec.push_back(i);
	if(turns) //Om det behövs...
		std::rotate(vec.begin(),vec.end()-turns,vec.end()); //...rotera
	int half=posses/2;
	vec.push_back(posses);
	for(int i=0;i<half;++i) {
		int j = half-1-i;
		cout << vec[posses-j-1] << '-' << vec[j] << endl;
	}
}
