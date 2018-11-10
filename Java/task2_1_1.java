public class task2_1_1 {
    public static boolean booleanExpression(boolean a, boolean b, boolean c, boolean d) {
        if (((a ^ b) && (c ^ d))   ||
            ((a && b) && !c && !d) ||
            (!a && !b && (c && d))) {
            return true;
        }
        return false;
    }
    public static void main(String args[]) {
        boolean a = booleanExpression(false, true, true, true);
        System.out.println(a);
    }
}