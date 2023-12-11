#include<stdio.h>

long Fact(long int  N){
    if(N == 0 || N == 1){
        return 1;
    }
    return Fact(N-1) * N ;
}
int main(void){
    long int n;
    printf("Enter n: ");
    scanf("%d",&n);
    long int res = Fact(n);
    printf("%d! = %d",n,res);
}