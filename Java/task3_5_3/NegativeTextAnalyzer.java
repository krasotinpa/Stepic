public class NegativeTextAnalyzer extends KeywordAnalyzer {
    private String[] keywords = {":(", "=(", ":|"};

    protected Label getLabel() {
        return Label.NEGATIVE_TEXT;
    }
    protected String[] getKeywords() {
        return this.keywords;
    }
}