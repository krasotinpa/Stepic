public class SpamAnalyzer extends KeywordAnalyzer {
    private String[] keywords;

    public SpamAnalyzer (String[] keywords) {
        String[] skey = new String[keywords.length];
        System.arraycopy(keywords, 0, skey, 0, skey.length);
        this.keywords = skey;
    }

    protected Label getLabel() {
        return Label.SPAM;
    }
    protected String[] getKeywords() {
        return this.keywords;
    }
}