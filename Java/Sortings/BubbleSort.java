package Java.Sortings;
import java.util.Scanner;
public class BubbleSort {
    public static void main(String[] args) {
        int n;
        int i,j;
        int temp;
        Scanner Sc = new Scanner(System.in);
        System.out.print("Enter no of elements: ");
        n = Sc.nextInt();
        int[] arr=new int[n];
        System.out.println("Enter elemnts into Array ---|");
        for(i=0;i<n;i++){
            arr[i] = Sc.nextInt();
        }
        System.out.println("--- Input Taken ---");
        for(i=0;i<n;i++){
            for(j=i;j<n;j++){
                if(arr[i]>arr[j]){
                    temp =arr[i];
                    arr[i] =arr[j];
                    arr[j] = temp;
                }
            }
        }
        System.out.print("Elements sorted in Accending Oreder => ");
        for(i=0;i<n;i++){
            System.out.print(arr[i]+" ");
        }
    }
}
