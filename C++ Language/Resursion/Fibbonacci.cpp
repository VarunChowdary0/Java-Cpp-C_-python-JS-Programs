#include<iostream>
using namespace std;

long long int Fibbo(int N){
    if (N == 0)
    {
        return 0;
    }
    else if (N == 1)
    {
        return 1;
    }
    
    return Fibbo(N-1) + Fibbo(N-2);
    
}
int main(void){
    int n;
    cout << "Enter N :" ;
    cin >> n;
    long res = Fibbo(n);
    cout << n << "th Fibonnacci Term = " << res;  
}