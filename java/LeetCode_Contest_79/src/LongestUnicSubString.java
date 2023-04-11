import java.util.Arrays;

public class LongestUnicSubString {
    public static void main(String[] args) {
    lengthOfLongestSubstring("abcabcbb");
    lengthOfLongestSubstring("bbbbb");
    lengthOfLongestSubstring("pwwkew");
    lengthOfLongestSubstring(" ");
    }

    public static int lengthOfLongestSubstring(String s) {
//        s = s.trim();
        String buffer = "";
        int max = 0;
        Integer temp;
        for (int i = 0; i < s.length(); i++) {
            temp = getInteger(i, s, buffer);
            if (temp > max) max = temp;
            buffer = "";
        }
        return max;
    }

    private static Integer getInteger(int index, String s, String temp) {
        for (int i = index; i < s.length(); i++) {
            if (!temp.toString().contains(String.valueOf(s.charAt(i)))) {
                temp += s.charAt(i);
            } else {
                return temp.length();
            }
        }
        return temp.length();
    }
}
