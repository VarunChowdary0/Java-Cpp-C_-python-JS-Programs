#include<stdio.h>

int main(void){
    int arr[100];
    int n;
    int i;
    int x;
    int found = 0;
    printf("Enter N.O elements: ");
    scanf("%d",&n);
    printf("Enter elements:  ");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("Input has Taken ...\n");
    printf("Enter element to be searched: ");
    scanf("%d",&x);
    for(i=0;i<n;i++){
        if(arr[i]==x){
            printf("Element is found at index %d !!",i);
            found = 1;
            break;
        }
    }
    if(!found){
        printf("Element not Found !!");
    }
}