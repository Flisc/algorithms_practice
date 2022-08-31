import java.util.*;
import java.util.stream.Collectors;

public class Problem2 {
    /**
     * 2284. Sender With Largest Word Count
     * https://leetcode.com/contest/biweekly-contest-79/problems/sender-with-largest-word-count/
     */
    public static void main(String[] args) {

        String[] messages;
        String[] senders;

        /**
         *  Input: messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]
         *           Output: "Alice"
         *           Explanation: Alice sends a total of 2 + 3 = 5 words.
         *           userTwo sends a total of 2 words.
         *           userThree sends a total of 3 words.
         *           Since Alice has the largest word count, we return "Alice".
         */
        messages = new String[]{"Hello userTwooo", "Hi userThree", "Wonderful day Alice", "Nice day userThree"};
        senders = new String[]{"Alice", "userTwo", "userThree", "Alice"};
        System.out.println(largestWordCount(messages, senders));

        /**
         *Input: messages = ["How is leetcode for everyone","Leetcode is useful for practice"], senders = ["Bob","Charlie"]
         * Output: "Charlie"
         * Explanation: Bob sends a total of 5 words.
         * Charlie sends a total of 5 words.
         * Since there is a tie for the largest word count, we return the sender with the lexicographically larger name, Charlie.
         */
        messages = new String[]{"How is leetcode for everyone", "Leetcode is useful for practice"};
        senders = new String[]{"Bob", "Charlie"};

        System.out.println(largestWordCount(messages, senders));
    }

    public static String largestWordCount(String[] messages, String[] senders) {
        HashMap<String, Integer> senderByWords = new HashMap<>();
        for (int i = 0; i < messages.length; i++) {
            if (senderByWords.containsKey(senders[i]))
                senderByWords.replace(senders[i], senderByWords.get(senders[i]) + messages[i].split(" ").length);
            else
                senderByWords.put(senders[i], messages[i].split(" ").length);
        }

        // key's from source map that have same values are mapped here as values for 1 key (value from source map).
        Map<Integer, ArrayList<String>> reverseMap = new HashMap<>(
                senderByWords.entrySet().stream()
                        .collect(Collectors.groupingBy(Map.Entry::getValue)).values().stream()
                        .collect(Collectors.toMap(
                                item -> item.get(0).getValue(),
                                item -> new ArrayList<>(
                                        item.stream()
                                                .map(Map.Entry::getKey)
                                                .collect(Collectors.toList())
                                ))
                        ));
        Optional<Integer> max = reverseMap.keySet().stream().max(Integer::compare);
        return max.isPresent()
                ? reverseMap.get(max.get()).stream()
                    .sorted(Comparator.comparing(String::length).reversed()
                            .thenComparing(String::compareTo))
                    .findFirst()
                    .orElseGet(null)
                : null;
    }
}
