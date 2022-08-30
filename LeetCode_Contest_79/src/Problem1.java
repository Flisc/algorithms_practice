import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Problem1 {
    /**
     * Check if Number Has Equal Digit Count and Digit Value
     * https://leetcode.com/contest/biweekly-contest-79/problems/check-if-number-has-equal-digit-count-and-digit-value/
     */
    public static void main(String[] args) {
        /**
         * Input: num = "1210"
         * Output: true
         * Explanation:
         * num[0] = '1'. The digit 0 occurs once in num.
         * num[1] = '2'. The digit 1 occurs twice in num.
         * num[2] = '1'. The digit 2 occurs once in num.
         * num[3] = '0'. The digit 3 occurs zero times in num.
         * The condition holds true for every index in "1210", so return true.
         */
        System.out.println(stringCheck("1210"));
        /**
         * Input: num = "030"
         * Output: false
         * Explanation:
         * num[0] = '0'. The digit 0 should occur zero times, but actually occurs twice in num.
         * num[1] = '3'. The digit 1 should occur three times, but actually occurs zero times in num.
         * num[2] = '0'. The digit 2 occurs zero times in num.
         * The indices 0 and 1 both violate the condition, so return false.
         */
        System.out.println(stringCheck("030"));
    }

    private static boolean stringCheck(final String num) {
        List<Character> collect = num.chars().mapToObj(c -> (char) c)
                .collect(Collectors.toList());
        for (int i = 0; i < collect.size(); i++) {
            if (checkFreq((char) (i + '0'), collect.get(i), collect) == false) return false;
            else continue;
        }
        return true;
    }

    private static boolean checkFreq(char index, char freq, List<Character> characters) {
        return characters.stream()
                .filter(character -> character == index)
                .count() == (freq - 48) ? true : false;
    }
}
