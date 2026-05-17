class Solution {
    public int total(int n1, int n2){
        return n1 + n2;
    }
    public int[] twoSum(int[] nums, int target) {
        int l = 0, r = nums.length - 1;

        while(l < r){
            if(total(nums[l], nums[r]) < target)
                l++;
            else if(total(nums[l], nums[r]) > target)
                r--;
            else
                return new int[] {l + 1, r + 1};
        }

        return new int[] {};
    }
}
