#include<stdio.h>

int main(void){
    int n;
    printf("Enter number of elements: ");
    scanf("%d",&n);
    int arr[n];
    int temp;
    int i,j,min_idx;
    printf("Enter elements into Array ||\n");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++){
        min_idx = i;
        for(j=i;j<n;j++){
            if(arr[min_idx] > arr[j]){
                min_idx = j;
            }
        }
        temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }

    for(i=0;i<n;i++){
        printf("%d ",arr[i]);
    }

}