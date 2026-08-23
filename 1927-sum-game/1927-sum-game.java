class Solution {
    public boolean sumGame(String num) {
        int sumDiff = 0;
        int questDiff = 0;
        int n = num.length();

        for (int i = 0; i < n; i++) {
            if (i < n / 2) {
                if (num.charAt(i) == '?') {
                    questDiff++;
                } else {
                    sumDiff += num.charAt(i) - '0';
                }
            } else {
                if (num.charAt(i) == '?') {
                    questDiff--;
                } else {
                    sumDiff -= num.charAt(i) - '0';
                }
            }
        }

        // Bob can only force a tie (win for Bob) if the total difference in '?' counts 
        // cancels out the sum difference at a rate of 9 per pair of '?' (i.e., 4.5 per '?').
        return sumDiff * 2 != -questDiff * 9;
    }
}