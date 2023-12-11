#include<stdio.h>

int Fiboo(int  N){
    if(N == 0 ){
        return 0;
    }
    else if(N == 1){
        return 1;
    }
    return Fiboo(N-1) + Fiboo(N-2) ;
}
int main(void){
    int n;
    printf("Enter n: ");
    scanf("%d",&n);
    int res = Fiboo(n);
    printf("%dth Fibbonacci Term = %d",n,res);
}