#include<iostream>
using namespace std;

bool checkPerfectNumber(int num) {
        int arr[num/2];
        int m=0;
        for (int i=1;i<num;i++)
        {
            if(num%i==0)
            {
                arr[m]=i;
                m++;
            }
        }
        int sum=0;
        for (int i=0;i<m;i++)
        {
            sum+=arr[i];
        }
        if(sum==num){
            return true;
        }
        else{
            return false;
        }
}
