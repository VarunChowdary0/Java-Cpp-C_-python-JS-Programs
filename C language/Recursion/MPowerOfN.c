#include<stdio.h>

long getPow(int base,int power){
    if (power == 1){
        return base;
    }
    return (base * getPow(base,power-1));
}
int main(void){
    int base;
    int power;
    printf("Enter base and power: ");
    scanf("%d%d",&base,&power);
    long int res = getPow(base,power);
    printf("%d^%d = %d",base,power,res);
}