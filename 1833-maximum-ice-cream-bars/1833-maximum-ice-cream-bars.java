class Solution {
    public int maxIceCream(int[] costs, int coins) {
        int c=0;
        Arrays.sort(costs);
        for (int num:costs){
            if(coins<num)
            break;
        c++;
        coins-=num;

        }
        return c;
    }
}