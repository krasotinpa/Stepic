import java.math.*;
import java.lang.*;

public class task2_4_1 {
    /**
     * Flips one bit of the given <code>value</code>.
     *
     * @param value     any number
     * @param bitIndex  index of the bit to flip, 1 <= bitIndex <= 32
     * @return new value with one bit flipped
     */
    public static BigInteger factorial(int value) {
        if (value == 1) {
            return BigInteger.ONE;
        }
        else {
            return factorial(value-1).multiply(BigInteger.valueOf(value));
        }
    }
    public static void main(String args[]) {
        for (int i = 1; i <= 10; i++) {
            System.out.println(i + " " + factorial(i).toString());
        }
    }
}