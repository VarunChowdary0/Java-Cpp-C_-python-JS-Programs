import java.util.Scanner;
public class BinarySearch {
    public static void main(String[] args) {
        int n;
        int x;
        int i;
        int start , mid ,  end;
        boolean found = false;
        Scanner Sc = new Scanner(System.in);
        System.out.print("Enter no of elements: ");
        n = Sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter elements in accending order --| ");
        for(i=0;i<n;i++){
            arr[i] = Sc.nextInt();
        }
        System.out.print("Enter number to be found: ");
        x = Sc.nextInt();
        start = 0;
        end = n;
        while(true){
            mid = (start+end)/2;
            if(x == arr[mid]){
                    System.out.println("Found at index "+mid+" !!");
                    found = true;
                    break;
            } 
            if(start == mid){
                break;
            }
            else if( x > arr[mid]){
                    start = mid;
            }
            else{
                    end = mid;
           }
        }
        if(!found){
            System.out.println("Not found !!");
        }
    }
}