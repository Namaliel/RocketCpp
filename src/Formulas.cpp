#include <stdio.h>
#include <math.h>
#include <vector>
#include <iostream>

double RawRise(double mass, double height)
{
    double g = 9.81;
    double result = g*mass*height;
    return result;
}

double Gravity(double earth, double height)
{
    double result;
    double constant = 6.67430e-11;
    temp = earth / pow(height,2);
    result = temp * constant;
    return result;
}

class Object
{
    public:
        std::vector<double> x;
        std::vector<double> y;
        std::vector<double> z;
}
