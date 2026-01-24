class Solution {
    public int[] solution(int a, int b, int c, int d) {
        int x = a*d+b*c;
        int y = b*d;
        
        // 약분
        int g = 1;
        int i = 2;
        int tx = x;
        int ty = y;
        while (i<=x && i<=y){
            if (x%i==0 && y%i==0){
                g = g*i;
                x = x/i;
                y = y/i;
            }
            else {
                i++;
            }
        }
        
        x = tx / g;
        y = ty / g;
        
        int[] answer = {x, y};
        return answer;
    }
}