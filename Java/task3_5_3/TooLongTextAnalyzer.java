public class TooLongTextAnalyzer implements TextAnalyzer {
    private int maxLength = 0;
    public TooLongTextAnalyzer(int maxLength) {
        this.maxLength = maxLength;
    }
    public Label processText(String text) {
        return (text.length() > this.maxLength ? Label.TOO_LONG : Label.OK);
    }
}
