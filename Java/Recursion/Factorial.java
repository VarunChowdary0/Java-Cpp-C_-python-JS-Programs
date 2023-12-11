package Java.Recursion;

import java.util.Scanner;

public class Factorial {

    public static long Fact(long N){
        if (N == 0 || N == 1) {
            return 1;
        }
        return Fact(N-1) * N;
    }
    public static void main(String[] args) {
        Scanner Sc= new Scanner(System.in);
        System.out.print("Enter n: ");
        int n = Sc.nextInt();
        long res = Fact(n);
        System.out.println(n+"! = "+res);
    }
}
