import java.util.Arrays;
import java.util.Collections;

public class MedianOfArrays {
    public static void main(String[] args) {
        System.out.println(findMedianSortedArrays(new int[]{1, 2}, new int[]{3, 4}));
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] merged = new int[nums1.length + nums2.length];
        int cursor = 0;
        int cursor1 = 0;
        int cursor2 = 0;
        while (cursor1 < nums1.length) {
            merged[cursor++] = nums1[cursor1++];
        }
        while( cursor2 < nums2.length) {
            merged[cursor++] = nums2[cursor2++];
        }
        Arrays.sort(merged);
        int length = merged.length;
        if (length % 2 == 0) {
            return  (merged[length / 2 -1] + merged[length / 2]  ) / 2d;
        } else {
            return merged[length/2];
        }
    }
}
