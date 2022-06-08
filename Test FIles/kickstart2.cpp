#include <iostream>
using namespace std;
int checkproduct(int n)
{
    int product = 1;
    while (n != 0)
    {
        product = product * (n % 10);
        n = n / 10;
    }
    return product;
}

int checkadd(int n)
{
    int sum = 0;
    while (n != 0)
    {
        sum = sum + n % 10;
        n = n / 10;
    }
    return sum;
}
int main()
{
    int t;
    cin >> t;
    int arr[t];
    for (int i = 0; i < t; i++)
    {
        int start, stop, count = 0;
        cin >> start >> stop;
        if (start == stop)
        {
            if (checkproduct(start) % checkadd(stop) == 0)
            {
                count = 1;
            }
        }
        else
        {
            for (int j = start; j < stop + 1; j++)
            {
                if (checkproduct(j) % checkadd(j) == 0)
                {
                    count++;
                }
            }
        }
        arr[i] = count;
    }
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: %d\n", i + 1, arr[i]);
    }
}