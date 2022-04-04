#include <iostream>
using namespace std;

int check(int s){
    int y=s-(-1);
    return (y*-1);    
}

int main()
{
    int t;
    cin>>t;
    int arr[t];
    for (int i = 0; i < t; i++)
    {
        int x,y,a,b;
        cin>>x;
        arr[i] =check(x);
    }
    for (int i = 0; i < t; i++)
    {
        cout<<arr[i]<<endl;
    }
    
}