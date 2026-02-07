class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int n = queries.length;
        int[] ans = new int[n]; // 정답배열을 쿼리 갯수만큼
       
        for(int i=0; i<n; i++){ // 각 쿼리
            int s = queries[i][0];
            int e = queries[i][1];
            int k = queries[i][2];
            
            int mn = 1000000;
            for(int j=s; j<=e; j++){
                if(arr[j]>k){
                    if(mn>arr[j]) mn=arr[j];
                }
            }
            
            if (mn==1000000) ans[i] = -1;
            else ans[i]=mn;
        }
        
        
        return ans;
    }
}