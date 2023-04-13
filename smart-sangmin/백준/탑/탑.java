import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

import java.util.Stack;
import java.util.StringTokenizer;

public class 탑 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] towers = new int[N];
        for (int i = 0; i < N; i++) {
            towers[i] = Integer.parseInt(st.nextToken());
        }

        Stack<Integer> stack = new Stack<>();
        stack.add(N - 1);
        int[] answer = new int[N];
        for (int i = N - 2; i >= 0; i--) {
            while (stack.size() > 0 && towers[stack.peek()] < towers[i]) {
                answer[stack.pop()] = i+1;
            }
            stack.push(i);
        }

        for (int a : answer) {
            System.out.print(a + " ");
        }
    }
}