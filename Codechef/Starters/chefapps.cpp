#include <iostream>
using namespace std;

int calc(int a, int b, int c, int d)
{

    int temp = a - b - c;
    if (temp >= d)
    {
        return 0;
    }
    else if ((((b + c)) >= a) || ((b + c) <= a))
    {
        if (((temp + b) >= d) || (temp + c) >= d)
            return 1;
        else{
            return 2;
        }
    }
    else
    {
        return 2;
    }
}

int main()
{
    int test, a, b, c, d;
    cin >> test;

    for (int i = 0; i < test; i++)
    {
        cin >> a >> b >> c >> d;
        cout << calc(a, b, c, d) << endl;
    }
}