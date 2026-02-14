import java.util.*;

class Solution {
    public int solution(int[] array) {
        int answer = 0;

        // 해쉬맵에 세팅
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int a: array) {
            map.put(a, map.getOrDefault(a, 0) + 1);
        }

        // 최대값 찾기
        int mx=0;
        for(int a: map.keySet()) {
            if (mx<map.getOrDefault(a, 0)){
                mx = map.getOrDefault(a, 0);
            }
        }

        // 최대값이 몇개인지
        int cnt = 0;
        for(int v: map.keySet()) {
            if (mx==map.get(v)) {
                answer = v;
                cnt++;
            }
        }

        if(cnt>1){
            answer = -1;
        }

        return answer;
    }
}
