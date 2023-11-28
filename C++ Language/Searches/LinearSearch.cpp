#include<iostream>
using namespace std;
int main(void){
    int n;
    int x;
    int i;
    cout << "Enter no of elements: ";
    cin >> n;
    int arr[n];
    bool found= false;
    cout << "Enter elements in accending, or decending order --| " << endl;
    for(i=0;i<n;i++){
        cin >> arr[i];
    }
    cout << "Enter number to be found: ";
    cin >> x;
    for(int i: arr){
        if(x == i){
            cout << "Found !!";
            found = true;
        }
    }
    if(!found){
        cout << "Element not Found !!";
    }
}