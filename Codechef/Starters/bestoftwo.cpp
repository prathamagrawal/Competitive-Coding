#include <iostream>
using namespace std;

int main(){
    int test,a,b,c,d;
    cin>>test;

    for (int i=0; i<test;i++) {
        cin>>a>>b>>c>>d;
        if((a!=c) && (b!=d)) {
            cout<<1<<endl;
        }
        else{
            cout<<2<<endl;
        }
    }
}