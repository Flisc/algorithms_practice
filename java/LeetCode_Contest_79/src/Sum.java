import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public class Sum {
    public static void main(String[] args) {
        /**
         * https://leetcode.com/problems/two-sum/
         *
         * Example 1:
         * Input: nums = [2,7,11,15], target = 9
         * Output: [0,1]
         * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
         */
        int[] nums = new int[]{2, 7, 11, 15};
        Optional<int[]> result;
        result = twoSum(nums, 9);
        printResult(result);
        /**
         * Example 2:
         *
         * Input: nums = [3,2,4], target = 6
         * Output: [1,2]
         */
        nums = new int[]{3, 2, 4};
        result = twoSum(nums, 6);
        printResult(result);
        /**
         * Example 3:
         *
         * Input: nums = [3,3], target = 6
         * Output: [0,1]
         */
        nums = new int[]{3, 3};
        result = twoSum(nums, 6);
        printResult(result);

    }

    private static Optional<int[]> twoSum(int[] nums, int target) {
        int[] result;
        List<Integer> list = Arrays.stream(nums).mapToObj(Integer::new).collect(Collectors.toList());
        for (int integer : list) {
            Optional<Integer> secondElem = checkArray(list, integer, target);
            if (secondElem.isPresent()
                    && !secondElem.isEmpty())
                return Optional.of(new int[]{list.indexOf(integer), secondElem.get()});
        }
        return Optional.empty();
    }

    private static Optional<Integer> checkArray(List<Integer> list, int currentElement, int target) {
        for (int i = list.indexOf(currentElement) + 1; i < list.size(); i++) {
            if (currentElement + list.get(i) == target) return Optional.of(new Integer(i));
        }
        return Optional.empty();
    }

    private static int checkArray2(int[] list, int currentIndex, int target) {
        for (int i = currentIndex + 1; i < list.length; i++) {
            if (list[currentIndex] + list[i] == target) return i;
        }
        return -1;
    }

    private static void printResult(Optional<int[]> result) {
        if (result.isPresent())
            System.out.println(Arrays.stream(result.get())
                    .mapToObj(Integer::new)
                    .collect(Collectors.toList())
                    .toString());
    }

    private static int[] leetCodeVersion(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            int secondElem = checkArray2(nums, i, target);
            if (secondElem != -1) return new int[]{i, secondElem};
        }
        return new int[]{};
    }
}
