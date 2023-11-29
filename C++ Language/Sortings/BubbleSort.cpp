#include<iostream>
using namespace std;
int main(void){
    int n;
    int i,j;
    int temp;
    cout << "Enter no of elements: ";
    cin >> n;
    int arr[n];
    cout << "Enter the elements into Array ----|" << endl;
    for(i=0;i<n;i++){
        cin >> arr[i];
    }
    for(i=0;i<n;i++){
        for(j=i;j<n;j++){
            if(arr[i]>arr[j]){
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    for(i=0;i<n;i++){
        cout << arr[i] << " ";
    }
}