class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder sb = new StringBuilder();
        
        for (String word : words) {
            int weightSum = 0;
            

            for (int i = 0; i < word.length(); i++) {
                weightSum += weights[word.charAt(i) - 'a'];
            }
            
            int rem = weightSum % 26;
            
            char mappedChar = (char) ('z' - rem);
            sb.append(mappedChar);
        }
        
        return sb.toString();
    }
}