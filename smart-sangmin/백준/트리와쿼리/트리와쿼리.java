import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class 트리와쿼리 {
    static ArrayList<ArrayList<Integer>> graph;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int Q = Integer.parseInt(st.nextToken());
        dp = new int[N + 1];
        graph = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 1; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int sNode = Integer.parseInt(st.nextToken());
            int eNode = Integer.parseInt(st.nextToken());
            graph.get(sNode).add(eNode);
            graph.get(eNode).add(sNode);
        }
        makeTree(R, -1);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < Q; i++) {
            int U = Integer.parseInt(br.readLine());
            sb.append(dp[U]).append("\n");
        }
        System.out.println(sb);
    }

    // dfs ?
    public static int makeTree(int cur, int parent) {
        dp[cur] = 1;
        for (int sub : graph.get(cur)) {
            if (sub == parent) {
                continue;
            }
            dp[cur] += makeTree(sub, cur);
        }
        return dp[cur];
    }
}
