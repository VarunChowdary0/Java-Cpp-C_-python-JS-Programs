package Java.Recursion;

import java.util.Scanner;

public class Fibbonacci {
     public static long Fibbo(int N){
        if (N == 0 )  {
            return 0;
        }
        else if( N == 1){
            return 1;
        }
        return Fibbo(N-1) + Fibbo(N-2);
    }
    public static void main(String[] args) {
        Scanner Sc= new Scanner(System.in);
        System.out.print("Enter n: ");
        int n = Sc.nextInt();
        long res = Fibbo(n);
        System.out.println(n+"th Fibbonacci Term: "+res);
    }
}
