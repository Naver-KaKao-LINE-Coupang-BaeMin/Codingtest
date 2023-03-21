import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Stack;
import java.util.StringTokenizer;

public class BOJ23294_웹브라우저1 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int q = Integer.parseInt(stringTokenizer.nextToken());
        int c = Integer.parseInt(stringTokenizer.nextToken());

        int[] cacheArray = new int[n];
        stringTokenizer = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            cacheArray[i] = Integer.parseInt(stringTokenizer.nextToken());
        }

        Deque<Integer> backwardStack = new LinkedList<>();
        Stack<Integer> frontwardStack = new Stack<>();
        int current = 0;
        int wholeCache = 0;
        boolean init = true;

        for (int i = 0; i < q; i++) {
            stringTokenizer = new StringTokenizer(br.readLine());
            String next = stringTokenizer.nextToken();
            if (next.equals("B")) {
                if (!backwardStack.isEmpty()) {
                    frontwardStack.push(current);
                    current = backwardStack.pop();
                }
            } else if (next.equals("F")) {
                if (!frontwardStack.isEmpty()) {
                    backwardStack.push(current);
                    current = frontwardStack.pop();
                }
            } else if (next.equals("A")) {
                while (!frontwardStack.isEmpty()) {
                    int temp = frontwardStack.pop();
                    wholeCache -= cacheArray[temp - 1];
                }

                if (init) {
                    init = false;
                } else {
                    backwardStack.push(current);
                }
                current = Integer.parseInt(stringTokenizer.nextToken());
                wholeCache += cacheArray[current - 1];

                while (wholeCache > c) {
                    int temp = backwardStack.pollLast();
                    wholeCache -= cacheArray[temp - 1];
                }
            } else if (next.equals("C")) {
                Deque<Integer> tempDeque = new LinkedList<>();

                //System.out.println(backwardStack);
                if (!backwardStack.isEmpty()) {
                    tempDeque.add(backwardStack.poll());
                }

                while (!backwardStack.isEmpty()) {
                    int temp = backwardStack.poll();
                    if (temp != tempDeque.peekLast()) {
                        tempDeque.add(temp);
                    } else {
                        wholeCache -= cacheArray[temp - 1];
                    }
                }

                //System.out.println(tempDeque);
                backwardStack = tempDeque;
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(current).append("\n");
        if (backwardStack.isEmpty()) {
            sb.append(-1);
        } else {
            while (!backwardStack.isEmpty()) {
                sb.append(backwardStack.pop()).append(" ");
            }
        }

        sb.append("\n");
        if (frontwardStack.isEmpty()) {
            sb.append(-1);
        } else {
            while (!frontwardStack.isEmpty()) {
                sb.append(frontwardStack.pop()).append(" ");
            }
        }

        System.out.println(sb);
    }
}
