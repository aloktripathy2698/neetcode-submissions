class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] res = new int[n];
        int hottest = 0;
        for(int i = n - 1; i >= 0 ; i--) {
            int currentTemp = temperatures[i];
            if(hottest <= currentTemp) {
                hottest = currentTemp;
                continue;
            }

            int days = 1;
            while(temperatures[i + days] <= currentTemp) {
                days += res[i + days];
            }

            res[i] = days;
        }

        return res;
        
    }
}
