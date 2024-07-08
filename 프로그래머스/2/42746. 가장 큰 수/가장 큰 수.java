import java.util.*;

class Solution {
    public String solution(int[] numbers) {
         // 숫자를 문자열로 변환하여 정렬
        //String[] numsAsStrings = Arrays.stream(numbers).mapToObj(String::valueOf).toArray(String[]::new);
        
        String[] answers = new String[numbers.length];
        
        // 2. 반복문을 사용하여 각 숫자를 문자열로 변환하여 배열에 저장
        for (int i = 0; i < numbers.length; i++) {
            answers[i] = String.valueOf(numbers[i]);
        }             
        
        // 정렬 기준 설정
        Arrays.sort(answers, (a, b) -> (b + a).compareTo(a + b));
        
        // 모든 숫자가 0인 경우 예외 처리
        if (answers[0].equals("0")) {
            return "0";
        }
        
        // 정렬된 문자열 배열을 이어붙여서 결과를 만듦
        return String.join("", answers);
    }
}