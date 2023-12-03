#include<iostream>
using namespace std;

int main(void){
    int n;
    int i,j;
    int temp;
    cout << "Enter no of terms: ";
    cin >> n;
    int arr[n];
    cout << "Enter elements into the Array " << endl ;
    for(i=0;i<n;i++){
        cin >> arr[i];
    }
    cout << "Input taken " << endl;
    for(i=1;i<n;i++){
        j=i;
        while( j>0 && (arr[j]<arr[j-1])){ // change the '<' <=>  '>'
            temp = arr[j-1];
            arr[j-1] = arr[j];
            arr[j] = temp ;
            j--;
        }
    }
    cout << "Elements sorted using Insertion Algorithem: ";
    for(i=0;i<n;i++){
        cout << arr[i] << " ";
    }
}