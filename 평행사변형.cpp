#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

double dist(int x1, int y1, int x2, int y2) {
    return sqrt(pow((double)x2 - x1, 2) + pow((double)y2 - y1, 2));
}

int main()
{
    int a_x1, a_y1, a_x2, a_y2, a_x3, a_y3; 
    cin >> a_x1 >> a_y1 >> a_x2 >> a_y2 >> a_x3 >> a_y3;
    
    if ((long long)(a_y2 - a_y1) * (a_x3 - a_x2) == (long long)(a_y3 - a_y2) * (a_x2 - a_x1))
    {
        cout << "-1.0\n";
        return 0;
    }

    double len_AB = dist(a_x1, a_y1, a_x2, a_y2);
    double len_BC = dist(a_x2, a_y2, a_x3, a_y3);
    double len_CA = dist(a_x3, a_y3, a_x1, a_y1);

    double l1 = 2.0 * (len_AB + len_CA); 
    double l2 = 2.0 * (len_AB + len_BC); 
    double l3 = 2.0 * (len_CA + len_BC); 
    
    double max_l = max({l1, l2, l3});
    double min_l = min({l1, l2, l3});
    
    cout.precision(10);
    cout << max_l - min_l << "\n";

    return 0;
}