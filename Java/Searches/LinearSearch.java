import java.util.Scanner;
class LinearSearch{
    public static void main(String[] args) {
        int n;
        int x;
        int i;
        boolean found = false;
        Scanner Sc = new Scanner(System.in);
        System.out.print("Enter no of elements: ");
        n = Sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements in accending, or decending order : ");
        for(i=0;i<n;i++){
            arr[i] = Sc.nextInt();
        }
        System.out.print("Enter element to be found: ");
        x = Sc.nextInt();
        for(i=0;i<n;i++){
            if(x == arr[i]){
                System.out.println("Found at index "+i+" !!");
                found =true;
            }
        }
        if(!found){
            System.err.println("Element not found !!");
        }
    }
}