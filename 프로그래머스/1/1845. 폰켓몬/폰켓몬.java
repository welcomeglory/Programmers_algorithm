import java.util.HashSet;

public class Solution {
    public int solution(int[] nums) {
        // 최대 선택 가능한 포켓몬의 수를 계산
        int max = nums.length / 2;

        // 중복을 제거하기 위해 HashSet을 사용
        HashSet<Integer> hashSet = new HashSet<>();

        // 배열을 순회하며 각 숫자를 HashSet에 추가
        for (int n : nums) {
            hashSet.add(n); // 중복된 숫자는 자동으로 제거됨
        }

        // 최대 선택 가능한 포켓몬의 수와 HashSet의 크기를 비교
        if (max >= hashSet.size()) {
            // 선택 가능한 수가 HashSet 크기보다 크거나 같으면, HashSet의 크기를 반환
            return hashSet.size();
        } else {
            // 선택 가능한 수가 HashSet 크기보다 작으면, 최대 선택 가능한 수를 반환
            return max;
        }
    }
}
