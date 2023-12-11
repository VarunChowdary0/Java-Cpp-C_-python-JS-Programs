#include<iostream>
using namespace std;

long Fact(long N){
    if (N == 0|| N== 1)
    {
        return 1;
    }
    return Fact(N-1) * N;
    
}
int main(void){
    int n;
    cout << "Enter N :" ;
    cin >> n;
    long res = Fact(n);
    cout << n << "! = " << res;  
}