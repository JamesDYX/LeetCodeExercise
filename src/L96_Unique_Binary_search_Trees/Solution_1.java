package L96_Unique_Binary_search_Trees;

public class Solution_1 {
    /*
    Catalan number
    (2n)!/(n!(n+1)!)
     */
    public int numTrees(int n) {
        long ans = 1;
        int k = n;
        n = 2*n;

        for(int i = 0  ; i < k ;i++){
            ans *=  (n-i);
            ans /=  (i+1);
        }
        return (int)(ans/(k+1));
    }
    public static void main(String[] args) {
        System.out.println(new Solution_1().numTrees(7));
    }
}
