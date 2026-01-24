class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        for(int i=0; i<numbers.length; i++){
            // i번째 == numbers[i]
            answer[i] = numbers[i]*2;
        }
        
        return answer;
    }
}