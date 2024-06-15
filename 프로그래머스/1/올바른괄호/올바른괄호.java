import java.util.*;

class Solution {
    public boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            
            if (ch == '(') {
                stack.push(ch);
            } else if (ch == ')') {
                if (stack.isEmpty()) {
                    return false;
                } else {
                    stack.pop();
                }
            }
        }
        
        // 모든 문자열을 검사한 후에 스택이 비어있어야 함
        return stack.isEmpty();
    }
}
