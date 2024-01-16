#include <iostream>
using namespace std;

int main() {
    int given;
    cin >> given;

    int arr[10] = {0, };

    while(given > 0) {
        if(given % 10 == 6) {
            if(arr[9] < arr[6])
                arr[9]++;
            else
                arr[6]++;
        } else if(given % 10 == 9) {
            if(arr[6] < arr[9])
                arr[6]++;
            else
                arr[9]++;
        } else {
            arr[given % 10]++;
        }
        given /= 10;
    }

    int largest = arr[0];
    for(int i=1; i<10; i++)
        largest = max(largest, arr[i]);

    cout << largest;

    return 0;
}