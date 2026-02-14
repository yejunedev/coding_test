import java.util.*;

class Solution {
    public int solution(int[] array) {
        int n = array.length;
        Arrays.sort(array); // 정렬
        // 중앙값 구하기
        int answer = array[n/2];
        return answer;
    }
}