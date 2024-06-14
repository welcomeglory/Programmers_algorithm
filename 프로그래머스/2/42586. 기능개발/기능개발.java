import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> q = new LinkedList<>();
        
        // 각 작업의 완료까지 필요한 일수 계산하여 큐에 저장
        for (int i = 0; i < progresses.length; i++) {
            int days = (int) Math.ceil((double) (100 - progresses[i]) / speeds[i]);
            q.offer(days);
        }
        
        List<Integer> answerList = new ArrayList<>();
        
        while (!q.isEmpty()) {
            int count = 1; // 첫 작업은 무조건 완료되므로 1로 초기화
            
            // 첫 작업 완료 기준으로 다음 작업들과 함께 완료되는지 체크
            int current = q.poll();
            while (!q.isEmpty() && current >= q.peek()) {
                q.poll(); // 동일 날짜에 완료되는 작업들은 카운트에 포함
                count++;
            }
            
            answerList.add(count);
        }
        
        // 리스트를 배열로 변환하여 반환
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = answerList.get(i);
        }
        
        return answer;
    }
}
