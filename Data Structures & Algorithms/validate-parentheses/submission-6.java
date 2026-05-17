class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> closeToOpen = new HashMap<>();

        closeToOpen.put(')', '(');
        closeToOpen.put(']', '[');
        closeToOpen.put('}', '{');

        Stack<Character> stack = new Stack<>();

        for(char c : s.toCharArray()) {
            if (stack.isEmpty() || !closeToOpen.containsKey(c) || stack.peek() != closeToOpen.get(c))
                stack.push(c);
            else
                stack.pop();
        }

        return stack.isEmpty();

    }
}
