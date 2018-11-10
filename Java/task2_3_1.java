import java.math.*;
import java.lang.*;

public class task2_3_1 {
    /**
     * Flips one bit of the given <code>value</code>.
     *
     * @param value     any number
     * @param bitIndex  index of the bit to flip, 1 <= bitIndex <= 32
     * @return new value with one bit flipped
     */
    public static boolean isPalindrome(String text) {
        StringBuilder strb = new StringBuilder(text.replaceAll("[\\W]", ""));

        return (new String(strb)).equalsIgnoreCase(new String(strb.reverse()));
    }
    public static void main(String args[]) {
        System.out.println(isPalindrome("Madam, I'm Adam!"));
    }
}