class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int n = queries.length;
        for(int j=0; j<n; j++){
            int s = queries[j][0];
            int e = queries[j][1];
            int k = queries[j][2];
            
            for(int i=s; i<=e; i++){
                if(i%k==0) { // i가 k배수이면
                    arr[i]++;
                }
            }
        }
        return arr;
    }
}