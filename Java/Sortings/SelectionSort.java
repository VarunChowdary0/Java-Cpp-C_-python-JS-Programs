package Java.Sortings;

import java.util.Scanner;

public class SelectionSort {
    public static void main(String[] args) {
        Scanner Sc = new Scanner(System.in);
        int i,j;
        int temp;
        int min_idx;
        System.out.print("Enter no of elements:  ");
        int n = Sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter elements into array ||");
        for(i=0;i<n;i++){
            arr[i] = Sc.nextInt();
        }
        System.out.println("Input Taken --------- ");
        for(i=0;i<n;i++){
            min_idx = i;
            for(j=i;j<n;j++){
                if(arr[min_idx] > arr[j]){
                    min_idx = j; 
                }
            }
            temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] =temp;
        }

        System.out.print("Elements sorted using Selection sort: ");
        for(i=0;i<n;i++){
            System.out.print(arr[i]+" ");
        }
    }
}
