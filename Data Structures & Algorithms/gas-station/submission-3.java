class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        int total_gas = 0, total_cost = 0;
        for(int i = 0; i < n; i++){
            total_gas += gas[i];
            total_cost += cost[i];
        }
        if(total_gas < total_cost)
            return -1;
        int curr_total = 0;
        int start = 0;
        for(int i = 0; i < n; i++){
            curr_total += gas[i] - cost[i];
            if(curr_total < 0){
                start = i + 1;
                curr_total = 0;
            }
        }
        return start;
    }
}
