#include <iostream>

using namespace std;

long long int a,b;

int main() {
    cin>>a>>b;
    if (a>=b) cout<<a-b;
    else cout<<b-a;
    return 0;
}