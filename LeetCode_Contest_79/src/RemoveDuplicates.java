public class RemoveDuplicates {
    public static void main(String[] args) {
        //https://leetcode.com/problems/remove-duplicates-from-sorted-array/
        removeDuplicates(new int[]{0, 1, 1, 2});
    }

    public static int removeDuplicates(int[] nums) {
        int counter = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    shiftToLeft(j, nums);
                    counter++;
                }
            }
        }


        return counter;
    }
    private static void shiftToLeft(int startIndex, int[] array) {
        for (int i = startIndex; i < array.length - 1; i++) {
            array[i] = array[i + 1];
        }
    }
}
