package L685_Redundant_Connection_II;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

public class Solution_1 {
    public int[] findRedundantDirectedConnection(int[][] edges) {

        int[] parents = new int[edges.length+1];
        int[] b = new int[]{0,0};
        for(int[] a:edges)
        {
            if(parents[a[1]]!=0)
            {
                b[0] = a[0];
                b[1] = a[1];
                continue;
            }
            parents[a[1]] = a[0];
        }


        return helper(parents,b,edges);
    }

    public int[] helper(int[] parents , int[] b , int[][] edges)
    {
        boolean[] seen = new boolean[edges.length+1];

        for(int i=1;i<=edges.length;i++)
        {
            if(parents[i]!=0 && !seen[i])
            {
                if(isMultiple(i,parents,seen,new boolean[edges.length+1]))
                {
                    if(b[0]==0)
                        return new int[]{parents[i],i};
                    else
                        return new int[]{parents[b[1]],b[1]};
                }
            }
        }

        return b;
    }

    public boolean isMultiple(int i , int[] parents , boolean[] seen , boolean[] vis)
    {
        if(vis[i])
            return true;
        if(seen[i])
            return false;
        seen[i] = true;
        vis[i] = true;
        if(parents[i]!=0)
            return isMultiple(parents[i],parents,seen,vis);
        return false;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        int[][] edges = {
                {1, 2},
                {2, 3},
                {3, 4},
                {4, 1},
                {1, 5}
        };
        int[] res = solution.findRedundantDirectedConnection(edges);
        System.out.println(Arrays.toString(res));
    }
}
