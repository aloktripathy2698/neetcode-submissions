class Solution {
    public int findPivotIndex(int[] nums){
        int l = 0, r = nums.length - 1;
        while (l < r){
            int m = l + (r - l) / 2;
            if (nums[m] > nums[nums.length - 1]){
                l = m + 1;
            } else {
                r = m;
            }
        }
        return r;
    }

    public int binarySearch(int[] nums, int l, int r, int target){
        while(l <= r){
            int m = l + (r - l) / 2;
            if(nums[m] == target){
                return m;
            } else if(nums[m] < target){
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return -1;
    }

    public int search(int[] nums, int target) {
        int pivotIdx = findPivotIndex(nums);
        int minElement = nums[pivotIdx];
        if (minElement == target){
            return pivotIdx;
        } else if (nums[pivotIdx] < target && target <= nums[nums.length - 1]){
            return binarySearch(nums, pivotIdx, nums.length - 1, target);
        } else {
            return binarySearch(nums, 0, pivotIdx - 1, target);
        }
    }
}
