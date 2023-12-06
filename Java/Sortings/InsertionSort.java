package Java.Sortings;
import java.util.Scanner;

public class InsertionSort {
    public static void main(String[] args) {
        Scanner Sc= new Scanner(System.in);
        int n;
        int i,j;
        int temp;
        System.out.print("Enter no of elements: ");
        n = Sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter elements into Array ");
        for(i=0;i<n;i++){
            arr[i] = Sc.nextInt();
        }
        System.out.println("Input Taken");
        for(i=1;i<n;i++){
            j = i;
            while ( j > 0 &&( arr[j-1] > arr[j])) {
                temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
                j--;
            }
        }
        System.out.print("Elements sorted using Insertion sort: ");
        for(i=0;i<n;i++){
            System.out.print(arr[i]+" ");
        }
    }
}
