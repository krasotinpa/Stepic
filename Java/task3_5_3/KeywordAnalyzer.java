public abstract class KeywordAnalyzer implements TextAnalyzer {

    protected abstract String[] getKeywords();    
    protected abstract Label getLabel();

    public Label processText(String text) {
        for (String k: this.getKeywords()) {
            if (text.contains(k)) {
                return this.getLabel();
            }
        }
        return Label.OK;
    }
}