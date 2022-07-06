// Pratham Agrawal
#include <vector>
#include <iostream>
using namespace std;

int main() {
	int test;
	cin>>test;
	
	for(int i = 0; i <test; i++) {
        int size,sum=0;
        cin>>size;
    
        vector <int> first(size),second(size);

        for (int j = 0; j < size; j++) {
            cin>>second[j];
            sum=sum + second[j];
        }
        sum=sum/(size+1);

        for(int j = 0; j < size; j++) {
            first[j]=second[j]-sum;
            cout<<first[j]<<" ";
        } 
        cout<<endl;
    }
}