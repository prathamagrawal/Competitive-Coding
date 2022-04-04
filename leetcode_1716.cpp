#include <iostream>
using namespace std;
int totalMoney(int n)
{
    int count = 0, temp =0;
    for (int i = 1; i <= n; i++)
    {
        count += (i % 8) + temp;
        cout<<(i % 7) + temp<<endl;
        if (i % 8 == 0)
        {
            temp += 1;
        }
    }
    return count;
}

int main()
{
    int n=10;
    int ans=totalMoney(n);
    cout<<ans<<endl;
}

