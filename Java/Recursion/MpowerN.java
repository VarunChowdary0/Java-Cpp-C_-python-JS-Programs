package Java.Recursion;

import java.util.Scanner;

public class MpowerN {
    public static int getPower(int base,int power){
        if(power == 0){
            return 1;
        }
        return getPower(base , power-1) * base;
    }
    public static void main(String[] args) {
        Scanner Sc = new Scanner(System.in);
        System.out.print("Enter N: ");
        int base = Sc.nextInt();
        int power = Sc.nextInt();
        int Res = getPower(base,power);
        System.out.println(base+"^"+power+" = "+Res);
    }
}
