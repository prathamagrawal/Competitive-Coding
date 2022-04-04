#include <iostream>
using namespace std;

int speed_typing(string orginial, string result)
{

    if (orginial.length() == result.length())
    {
        if (orginial == result)
        {
            return 1;
        }
        else{
            return -1;
        }
    }
    else if (orginial.length()<=result.length())
    {
        int count;
        for (int i=0; i<orginial.length(); i++)
        {
            if(orginial[i]!=result[i])
            {

            }
        }
    }
    
}

int main()
{
    int t;
    cin >> t;
    int arr[t];
    for (int i = 0; i < t; i++)
    {
        string orginial, result;
        arr[i] = speed_typing(orginial, result);
    }
}