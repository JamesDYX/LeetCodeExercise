package L62_Unique_Paths;

public class Solution_1 {
    public int uniquePaths(int m, int n) {
        int[] memory = new int[n];
        for (int i=0; i<n; i++) memory[i] = 1;
        for (int i=1; i<m; i++)
            for (int j=1; j<n; j++) memory[j] += memory[j-1];
        return memory[n-1];
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        System.out.println(solution.uniquePaths(7, 3));
    }
}
