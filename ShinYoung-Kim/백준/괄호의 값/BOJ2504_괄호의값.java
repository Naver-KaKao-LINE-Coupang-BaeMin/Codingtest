import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class BOJ2504_괄호의값 {
    final static int LEFT_CIRCLE = -1;
    final static int RIGHT_CIRCLE = -2;
    final static int LEFT_SQUARE = -3;
    final static int RIGHT_SQUARE = -4;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        Stack<Integer> stack = new Stack<>();
        int answer = 0;

        for (int i = 0; i < input.length(); i++) {
            char current = input.charAt(i);
            if (!stack.isEmpty()) {
                if (current == '(' || current == '[') {
                    pushStack(current, stack);
                } else if (current == ')') {
                    right(stack, LEFT_CIRCLE, 2);
                } else if (current == ']') {
                    right(stack, LEFT_SQUARE, 3);
                }
            } else {
                pushStack(current, stack);
            }
        }

        while (!stack.isEmpty()) {
            int temp = stack.pop();
            if (temp < 0) {
                finish();
            }
            answer += temp;
        }

        System.out.println(answer);
    }

    private static void pushStack(char current, Stack<Integer> stack) {
        switch (current) {
            case '(':
                stack.push(LEFT_CIRCLE);
                break;
            case ')':
                stack.push(RIGHT_CIRCLE);
                break;
            case '[':
                stack.push(LEFT_SQUARE);
                break;
            case ']':
                stack.push(RIGHT_SQUARE);
                break;
        }
    }

    private static void finish() {
        System.out.println(0);
        System.exit(0);
    }

    private static void right(Stack<Integer> stack, int circleOrSquare, int number) {
        int temp = 0;
        while (true) {
            if (stack.isEmpty()) {
                finish();
            }

            int before = stack.pop();
            if (before == circleOrSquare) {
                if (temp == 0) {
                    stack.push(number);
                } else {
                    stack.push(temp * number);
                }
                break;
            } else if (before > 0) {
                temp += before;
            } else {
                finish();
            }
        }
    }
}
