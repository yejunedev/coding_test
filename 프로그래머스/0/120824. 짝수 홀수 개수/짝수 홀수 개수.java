class Solution {
    public int[] solution(int[] num_list) {
        
        int hol = 0;
        int zza = 0;
        
        for(int i = 0; i < num_list.length; i++){
            if (num_list[i] % 2 == 0){
                zza++;
            } else {
                hol++;
            }
        }
        
        return new int[]{zza, hol};
    }
}