import java.util.function.DoubleUnaryOperator;

public class task3_5_1 {

    //метод левых прямоугольников
    public static void main(String[] args) {
        System.out.println(integrate(x -> 1, 0, 10));//10.0
        System.out.println(integrate(x -> x + 2, 0, 10));//70.0
        System.out.println(integrate(x -> Math.sin(x) / x , 1, 5));//0.603848
    }
    public static double integrate(DoubleUnaryOperator f, double a, double b) {
        double delta = 1;
        double eps = 1e-7;
        double res = 0, res1 = 0;

        do {
            res = res1;
            res1 = integrate(f, a, b, delta);
            delta /= 2.0;
        } while (Math.abs(res - res1) > eps);

        return res1;
    }
    public static double integrate(DoubleUnaryOperator f, double a, double b, double delta) {
        double res = 0.0;

        while (a < b) {
            res += f.applyAsDouble(a+delta) * delta;
            a += delta;
        }

        return res;
    }
}