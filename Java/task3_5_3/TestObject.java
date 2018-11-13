public class TestObject {
    public Label checkLabels(TextAnalyzer[] analyzers, String text) {
        for (TextAnalyzer a: analyzers) {
            Label L = a.processText(text);
            if (L != Label.OK) {
                return L;
            }
        }
        return Label.OK;
    }
}