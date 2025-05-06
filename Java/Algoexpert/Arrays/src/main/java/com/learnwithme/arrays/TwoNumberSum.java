package com.learnwithme.arrays;

public class TwoNumberSum {
    public static int[] twoNumberSumSimple(int[] array, int targetSum) {
        // This is a simple solution with O(n^2) time complexity
        // and O(1) space complexity.
        for (int i = 0; i < array.length - 1; i++) {
            for (int j = 1; j < array.length; j++) {
                if (array[i] + array[j] == targetSum) {
                    return new int[] {array[i], array[j]};
                }
            }
        }
        return new int[0];
    }
}
