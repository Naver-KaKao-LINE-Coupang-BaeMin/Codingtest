import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 사회망서비스 {
    static ArrayList<ArrayList<Integer>> graph;
    static int[][] dp;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        dp = new int[N + 1][2];
        for (int i = 1; i < N + 1; i++) {
            dp[i][0] = 0;
            dp[i][1] = 1;
        }

        graph = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        gogo(1, -1);
        int answer = Math.min(dp[1][0], dp[1][1]);
        System.out.println(answer);
    }

    public static void gogo(int cur, int parent) {
        for (int node : graph.get(cur)) {
            if (node == parent) {
                continue;
            }
            gogo(node, cur);
            dp[cur][0] += dp[node][1];
            dp[cur][1] += Math.min(dp[node][0], dp[node][1]);
        }
    }
}
