class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n=nums.length;
        int minlen=Integer.MAX_VALUE;
        int left=0;
        int cs=0;
        for (int right=0;right<n;right++){
            cs+=nums[right];
            while (cs>=target){
                minlen=Math.min(minlen,right-left+1);
                cs-=nums[left];
                left++;
            }
        }
       return minlen == Integer.MAX_VALUE ? 0 : minlen;
    }
}