
public class AsciiCharSequence implements CharSequence {
    private byte[] sequence;

    public AsciiCharSequence(byte[] s) {
        this.sequence = new byte[s.length];
        System.arraycopy(s, 0, this.sequence, 0, s.length);
    }
    public char charAt(int i) {
        return (char)this.sequence[i];
    }
    public int length() {
        return this.sequence.length;
    }
    public AsciiCharSequence subSequence(int begin, int end) {
        if (begin > end || begin < 0 || end > this.sequence.length)
            throw new IndexOutOfBoundsException();
        byte[] sub = new byte[end-begin];
        System.arraycopy(this.sequence, begin, sub, 0, end - begin);

        return new AsciiCharSequence(sub);
    }
    public String toString() {
        return new String(this.sequence);
    }
}
