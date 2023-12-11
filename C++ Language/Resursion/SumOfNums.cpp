#include<iostream>
using namespace std;

int getSum(int N){
    if(N == 0){
        return 0;
    }
    return getSum(N-1) + N;
}
int main(void){
    int n;
    cout <<"Enter N:  ";
    cin >> n;
    int Res = getSum(n);
    cout << "Sum : " << Res;
}