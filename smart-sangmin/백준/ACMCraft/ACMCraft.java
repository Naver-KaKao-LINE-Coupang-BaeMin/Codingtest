import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class ACMCraft {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int t = 0; t < T; t++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken()), K = Integer.parseInt(st.nextToken());

            int[] D = new int[N + 1];
            ArrayList<Integer>[] dependency = new ArrayList[N + 1];
            int[] link = new int[N + 1];
            st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= N; i++) {
                D[i] = Integer.parseInt(st.nextToken());
                dependency[i] = new ArrayList<>();
            }
            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                int first = Integer.parseInt(st.nextToken()), next = Integer.parseInt(st.nextToken());
                dependency[first].add(next);
                link[next]++;
            }

            Queue<Integer> q = new LinkedList<>();
            for (int i = 1; i <= N; i++) {
                if (link[i] == 0) {
                    q.add(i);
                }
            }

            int[] answer = new int[N + 1];
            while (!q.isEmpty()) {
                int node = q.poll();
                for (int next : dependency[node]) {
                    link[next]--;
                    if (link[next] == 0) {
                        q.add(next);
                    }
                    answer[next] = Math.max(answer[next], answer[node] + D[node]);
                }
            }
            int W = Integer.parseInt(br.readLine());
            sb.append(answer[W] + D[W]).append("\n");
        }
        System.out.println(sb);
    }
}