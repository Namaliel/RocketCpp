#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>

int factorial(int x)
{
    unsigned long long c = 1;
    for(int i=1; i<=x; i++)
    {
        c *= i;
    }
    return c;
}

int binomios(int a, int b, int n)
{
    double temp, result;
    for(int k=0;k<=n;k++)
    {
        long long int ax, bx, sub;
        sub  = factorial(k) * factorial(n-k);
        temp = factorial(n)/sub;
        ax = pow(a,n-k);
        bx = pow(b,k);
        result += temp*ax*bx;
    }
    return result;
}

double root(int a, int b, double n, int iterations)
{
    double temp, result;
    for(int k=0;k<=iterations;k++)
    {
        long long int ax, bx, sub;
        sub = factorial(k) * factorial(n-k);
        temp = factorial(n)/sub;
        ax = pow(a,n-k);
        bx = pow(b,k);
        result += temp*ax*bx;
    }
    return result;
}

int main()
{
    int a,b,i;
    double n;
    std::cin>>a>>b>>n>>i;
    std::cout<<root(a,b,n,i);
}
