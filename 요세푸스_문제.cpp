#include <iostream>
#include <vector>

using namespace std;

int n,k;
int idx = 0;

int main()
{
    cin >> n >> k;
    
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        arr[i] = i + 1;
    }
    
    vector<int> result;

    while (!arr.empty())
    {
        idx = (idx + k - 1) % arr.size(); 
        result.push_back(arr[idx]);
        arr.erase(arr.begin() + idx);
    }

    cout << "<";
    for (size_t i = 0; i < result.size(); ++i) {
        cout << result[i];
        if (i != result.size() - 1) {
            cout << ", ";
        }
    }
    cout << ">\n";
    
    return 0;
}