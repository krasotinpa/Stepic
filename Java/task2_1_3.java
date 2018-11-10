import java.math.*;

public class task2_1_3 {
    public static boolean doubleExpression(double a, double b, double c) {
        return Math.abs(a + b - c) < 1e-4;
    }
    public static void main(String args[]) {
        boolean a = doubleExpression(0.1, 0.2, 0.3);
        System.out.println(a);
    }
}