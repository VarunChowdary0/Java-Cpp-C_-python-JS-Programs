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
    for(i=1;i<n;i++){
        j = i;
        while (j>0 && (arr[j-1] > arr[j]))
        {
            temp = arr[j-1];
            arr[j-1] = arr[j];
            arr[j] = temp;
            j--;
        }   
    }
    printf("Sorted in accending order -> ");
    for(i=0;i<n;i++){
        printf("%d ",arr[i]);
    }
}