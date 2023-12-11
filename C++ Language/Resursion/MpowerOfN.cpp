#include<iostream>
using namespace std;

long getPower(int base,int power){
    if (power == 0)
    {
        return 1;
    }
    return getPower(base,power-1) * base;
    
}
int main(void){
    int base,power;
    cout << "Enter base and power :" ;
    cin >> base >> power;
    long res = getPower(base,power);
    cout << base << "^" << power << " = "<< res;  
}