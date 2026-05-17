class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1;
        int r = Arrays.stream(piles).max().getAsInt();
        int minSpeed = r;
        while(l <= r){
            int speed = l + (r - l) / 2;
            int time = 0;
            for(int pile: piles){
                time += Math.ceil((double) pile / speed);
            }

            if (time <= h){
                r = speed - 1;
                minSpeed = speed;
            } else {
                l = speed + 1;
            }
        }
        return minSpeed;
    }
}
