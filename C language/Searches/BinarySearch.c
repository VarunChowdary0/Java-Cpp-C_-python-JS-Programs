#include<stdio.h>
int main(void){
    int arr[100];
    int n;
    int i;
    int x;
    int start,mid,end;
    int found = 0;
    printf("Enter no of Elememts: ");
    scanf("%d",&n);
    printf("Enter elememts in accending order: ");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("Enter the number needed to be found: ");
    scanf("%d",&x);
    start = 0;
    end = n;
    while(1){
        mid = (start + end )/2;
        if(arr[mid] == x){
            printf("Found at index %d !!",mid);
            found = 1;
            break;
        }
        if(start == mid){
            break;
        }
        else if(x < arr[mid]){
            end = mid;
        }
        else{
            start = mid;
        }
    }
    if(!found){
        printf("Not found !!");
    }
}