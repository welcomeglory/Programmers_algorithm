import java.util.HashMap;

public class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> clothesMap = new HashMap<>();

        // 각 의상 종류별로 개수를 센다
        for (String[] cloth : clothes) {
            String kind = cloth[1];
            clothesMap.put(kind, clothesMap.getOrDefault(kind, 0) + 1);
        }

        // 각 종류별로 의상을 선택하는 경우의 수를 계산
        int combinations = 1;
        for (int count : clothesMap.values()) {
            combinations *= (count + 1);
        }

        // 아무 것도 입지 않는 경우를 뺀다
        return combinations - 1;
    }

}
