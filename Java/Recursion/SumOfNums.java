package Java.Recursion;

import java.util.Scanner;

public class SumOfNums {
    public static int getSum(int N){
        if(N == 0){
            return 0;
        }
        return getSum(N-1) + N;
    }
    public static void main(String[] args) {
        Scanner Sc = new Scanner(System.in);
        System.out.print("Enter N: ");
        int n = Sc.nextInt();
        long Res = getSum(n);
        System.out.println("Sum: "+Res);
    }
}