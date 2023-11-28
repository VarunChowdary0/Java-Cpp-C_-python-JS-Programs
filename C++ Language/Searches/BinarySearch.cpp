#include<iostream>
using namespace std;
int main(void){
    int n;
    int x;
    int i;
    int start,mid,end;
    bool found = false;
    cout << "Enter no of elements: ";
    cin >> n;
    int arr[n];
    cout << "Enter elements in accending order  --|" << endl;
    for(i==0;i<n;i++){
        cin >> arr[i];
    }
    cout << "Enter the element needed tobe found: ";
    cin >> x ; 
    start = 0;
    end = n;
    while(true){
        mid = (start + end) / 2;
        if(x == arr[mid]){
            cout << "Found at index " << mid << " !!" << endl;
            found = true;
            break;
        }
        if(start == mid){
            break;
        }
        else if( x > arr[mid]){
            start = mid;
        }
        else{
            end = mid;
        }
    }
    if(!found){
        cout << "Element not Found !!";
    }
}