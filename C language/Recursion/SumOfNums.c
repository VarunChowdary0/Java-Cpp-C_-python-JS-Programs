#include<stdio.h>

int getSum(int N){
    if(N==0){
        return 0;
    }
    return getSum(N-1) + N;
}
int main(void){
    int n;
    printf("Enter n: ");
    scanf("%d",&n);
    int Res = getSum(n);
    printf("Sum: %d",Res);
}
