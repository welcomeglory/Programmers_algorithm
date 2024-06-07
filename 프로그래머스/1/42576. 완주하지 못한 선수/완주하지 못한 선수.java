import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();

        // 참가자 명단을 HashMap에 추가
        for (String player : participant) {
            if (hm.containsKey(player)) {
                // 이미 존재하는 키인 경우 값을 1 증가시킴
                hm.put(player, hm.get(player) + 1);
            } else {
                // 존재하지 않는 키인 경우 값을 1로 설정
                hm.put(player, 1);
            }
        }

        // 완주자 명단을 통해 HashMap 업데이트
        for (String player : completion) {
            // 완주자의 수를 1 감소시킴
            if (hm.containsKey(player)) {
                hm.put(player, hm.get(player) - 1);
            }
        }

        // HashMap을 순회하며 값이 0이 아닌 참가자 찾기
        for (String key : hm.keySet()) {
            if (hm.get(key) != 0) {
                answer = key;
                break;
            }
        }

        return answer;
    }
}
