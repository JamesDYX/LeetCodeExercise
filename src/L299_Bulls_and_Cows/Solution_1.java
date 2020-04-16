package L299_Bulls_and_Cows;

public class Solution_1 {
    public String getHint(String secret, String guess) {
        int[] secret_counter = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        int[] guess_counter = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        int bullCounter = 0;
        for(int i=0; i<secret.length(); i++){
            if(secret.charAt(i) == guess.charAt(i)){
                bullCounter++;
            }
            else{
                secret_counter[secret.charAt(i)-'0']++;
                guess_counter[guess.charAt(i)-'0']++;
            }
        }
        int cowCounter = 0;
        for(int i=0; i<10; i++){
            cowCounter += Math.min(secret_counter[i], guess_counter[i]);
        }
        return bullCounter + "A" + cowCounter + "B";
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        System.out.println(solution.getHint("1123", "0111"));
    }
}
