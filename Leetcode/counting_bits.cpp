#include <iostream>
#include <vector>
#include <iterator>
using namespace std;

vector <int> countBits(int n){
    vector <int> arr;
        
        for (int i=0;i<n;i++){
            unsigned int uCount;
            uCount = i - ((i >> 1) & 033333333333) - ((i >> 2) & 011111111111);
            arr.push_back (((uCount + (uCount >> 3)) & 030707070707) % 63);

        }
        
    return arr;
}

int main()
{
    vector <int> nums=countBits(5);
    for(int i=0;i<nums.size();i++){
        cout<<nums[i]<<" "<<endl;
    }
}