import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 숨바꼭질3 {
    static int N, K;
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        N = Integer.parseInt(stringTokenizer.nextToken());
        K = Integer.parseInt(stringTokenizer.nextToken());
        bfs();
        System.out.println(answer);
    }

    public static void pprint(int[] a) {
        for (int b : a) {
            System.out.print(b + " ");
        }
    }

    // 왜? 안 됨?
    public static void bfs() { // 44프로 안됨,
        Queue<int[]> q = new LinkedList<>();
        boolean[] visited = new boolean[100001];
        q.add(new int[]{N, 0});
        visited[N] = true;
        while (!q.isEmpty()) {
            int[] temp = q.poll();
            int location= temp[0] , time = temp[1];
            if (location == K)
                answer = Math.min(answer, time);
            for (int m : new int[]{location * 2, location - 1, location + 1}) {
                if (0 <= m && m < 100001 && !visited[m]) {
                    q.add(new int[]{m, time + (m == (location * 2) ? 0 : 1)});
                    visited[m] = true;
                }
            }
        }
    }
}
