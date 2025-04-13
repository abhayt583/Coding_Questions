class Solution {
    private static final int MOD = (int) (1e9 + 7);
    public long powMOD(long x, long num){
        if (num == 0){
            return 1;
        } else if (num % 2 ==0){
            return powMOD(x * x % MOD, num / 2);
        } else {
            return x * powMOD(x, num - 1) % MOD;
        }
    }
    public int countGoodNumbers(long n) {
        if (n % 2 == 0){
            return (int) (powMOD(20, n / 2) % MOD);
        }
        return (int)(5 * powMOD(20, n / 2) % MOD);
    }
}
