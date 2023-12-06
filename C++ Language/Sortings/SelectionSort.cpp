#include<iostream>
using namespace std;

int main(void){
    int n;
    int i,j;
    int temp;
    cout << "Enter N: ";
    cin >> n ;
    int min_idx ;
    int arr[n];
    cout << "Enter Elements into Array ||" << endl;
    for(i=0;i<n;i++){
        cin >> arr[i];
    }
    cout << "Input Taken ---- " << endl;
    for(i=0;i<n;i++){
        min_idx = i;
        for(j=i;j<n;j++){
            if(arr[min_idx] > arr[j]){
                min_idx = j;
            }
        }
        temp = arr[i];
        arr[i] = arr[min_idx];
        arr[min_idx] = temp;
    }

    cout << "Sorted : ";
    for(i=0;i<n;i++){
        cout << arr[i] << " ";
    }
}
