import java.util.AbstractList;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class IpAddress {
    public static void main(String[] args) {
//        https://leetcode.com/problems/restore-ip-addresses/solutions/
//        System.out.println(restoreIpAddresses("25525511135"));
//        System.out.println(restoreIpAddresses("0000"));
        System.out.println(restoreIpAddresses("000000"));
    }

    public static List<String> restoreIpAddresses(String s) {
        List<String> res = new ArrayList<>();
        if (null == s || s.length() == 0) {
            return res;
        }
        StringBuilder builder = new StringBuilder();
        Predicate<Integer> limitPredicate = value -> value >= 0 && value <= 255;
       if(s.length() == 4) {
           char[] chars = s.toCharArray();
           for (int i=0; i < chars.length; i++) {
               if(chars[i] >= 0 && chars[i] <= 255) {
                   if(i == chars.length - 1) {
                       builder.append(chars[i]);
                   } else {
                       builder.append(chars[i] + ".");
                   }
               }
           }
           res.add(builder.toString());
       }
       else {
           char[] chars = s.toCharArray();
          String number;
           for ( int i = 0; i < chars.length; i++) {
                res.add(findNextNumber(String.valueOf(chars[i]), s));
           }
       }
        return res;
    }

    private static String findNextNumber(String currentString, String fullString) {
        Integer intVal = Integer.valueOf(currentString);
        do {
            int index = fullString.indexOf(currentString);
            currentString += fullString.substring(index, index +1);
        } while ( Integer.valueOf(currentString) < 255 );
        return  currentString;
    }
}
