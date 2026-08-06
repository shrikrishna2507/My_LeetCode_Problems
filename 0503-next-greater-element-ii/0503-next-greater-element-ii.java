import java.util.Arrays;
import java.util.Stack;

class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        Arrays.fill(result, -1);
        
        // Monotonic stack storing indices
        Stack<Integer> stack = new Stack<>();
        
        // Loop through the array twice to simulate circular behavior
        for (int i = 0; i < 2 * n; i++) {
            int currentIndex = i % n;
            
            while (!stack.isEmpty() && nums[stack.peek()] < nums[currentIndex]) {
                result[stack.pop()] = nums[currentIndex];
            }
            
            // Only push indices during the first pass
            if (i < n) {
                stack.push(currentIndex);
            }
        }
        
        return result;
    }
}