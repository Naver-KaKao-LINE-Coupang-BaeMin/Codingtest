import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ16207_직사각형 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        int[] stickArray = new int[n];

        for (int i = 0; i < n; i++) {
            stickArray[i] = Integer.parseInt(stringTokenizer.nextToken());
        }

        Arrays.sort(stickArray);
        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new LinkedList<>();

        for (int i = n - 1; i >= 0; i--) {
            if (visited[i]) {
                continue;
            }

            for (int j = i - 1; j >= 0; j--) {
                int current = stickArray[i];
                int before = stickArray[j];
                if (current - before >= 2) {
                    break;
                }

                if (visited[j]) {
                    continue;
                }

                if (current == before || current - 1 == before) {
                    visited[i] = true;
                    visited[j] = true;
                    queue.add(before);
                    break;
                }
            }
        }

        int queueSize = queue.size();
        int squareNumber = queueSize / 2;

        if (queueSize < 2) {
            System.out.println(0);
        } else {
            long answer = 0;
            for (int i = 0; i < squareNumber; i++) {
                int bigger = queue.poll();
                int smaller = queue.poll();
                answer += (long) bigger * smaller;
            }
            System.out.println(answer);
        }
    }
}
