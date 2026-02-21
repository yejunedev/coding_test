import java.util.*;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 1; i <= n; i+=2) {
            arr.add(i);
        }
        int[] answer  = arr.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}