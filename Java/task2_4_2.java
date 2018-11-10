import java.math.*;
import java.util.Arrays;
import java.lang.*;

public class task2_4_2 {
    /**
     * Flips one bit of the given <code>value</code>.
     *
     * @param value     any number
     * @param bitIndex  index of the bit to flip, 1 <= bitIndex <= 32
     * @return new value with one bit flipped
     */
    public static int[] mergeArrays(int[] a1, int[] a2) {
        int[] merge = new int[a1.length + a2.length];
        int i1 = 0, i2 = 0;

        for (int k = 0; k < merge.length; k++) {
            if (i1 > a1.length-1) {
                merge[k] = a2[i2];
                i2++;
            }
            else if (i2 > a2.length-1) {
                merge[k] = a1[i1];
                i1++;
            }
            else if (a1[i1] < a2[i2]) {
                merge[k] = a1[i1];
                i1++;
            }
            else {
                merge[k] = a2[i2];
                i2++;
            }
        }
            return merge; // your implementation here
    }
    public static void main(String args[]) {
        int[] a1 = {0};
        int[] a2 = {0, 1, 3};
        
        System.out.println(Arrays.toString(mergeArrays(a1, a2)));
    }
}