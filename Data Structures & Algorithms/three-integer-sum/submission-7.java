class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for(int i = 0; i < nums.length; i++){
            if(i > 0 && (nums[i - 1] == nums[i]))
                continue;
            int left = i + 1, right = nums.length - 1;
            while(left < right){
                if(nums[i] + nums[left] + nums[right] == 0){
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while(left < right && nums[left] == nums[left + 1])
                        left++;
                    left++;
                    while(left < right && nums[right] == nums[right - 1])
                        right--;
                    right--;
                }

                else if(nums[i] + nums[left] + nums[right] < 0){
                    while(left < right && nums[left] == nums[left + 1])
                        left++;
                    left++;
                }

                else{
                    while(left < right && nums[right] == nums[right - 1])
                        right--;
                    right--;
                }

            }
            
        }
        return res;
    }
}
