#include<stdio.h>
int main(void){
    int n;
    int i,j;
    int temp;
    printf("Enter n: ");
    scanf("%d",&n);
    int arr[n];
    printf("Enter elements into Array ---| \n");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("---- Input taken --- \n");
    for(i=0;i<n;i++){
        for(j=i;j<n;j++){
            if(arr[i]>arr[j]){
                temp = arr[j];
                arr[j] =arr[i];
                arr[i] = temp;
            }
        }
    }
    printf("Sorted in accending order -> ");
    for(i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}