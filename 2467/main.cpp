#include <iostream>

using namespace std;

int N;
int arr[100001];
int a, b;

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    int left = 0;
    int right = N - 1;

    int resLiquid = abs(arr[left] + arr[right]);
    a = arr[left];
    b = arr[right];

    while (left < right) {
        int tmp = arr[left] + arr[right];
        if (abs(tmp) < resLiquid) {
            resLiquid = abs(tmp);
            a = arr[left];
            b = arr[right];
        }

        if (tmp < 0)
            left++;
        else
            right--;
    }
    cout << a << " " << b << "\n";
}