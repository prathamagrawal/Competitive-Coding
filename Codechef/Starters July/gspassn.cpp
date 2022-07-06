#include <iostream>
#include <unordered_map>
using namespace std;

bool assignment(unordered_map<int,int> &testmap){
    for (auto x:testmap){
        if(x.second % x.first!=0){
            return false;
        }
    }
    return true;
}

int main(){
    int test,size,temp;
    cin>>test;
    for (int i=0; i<test;i++){
        cin>>size;
        unordered_map<int,int> tempmap;
        for (int j=0; j<size;j++){
            cin>>temp;
            tempmap[temp]++;
        }
        if(assignment(tempmap)){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }
}