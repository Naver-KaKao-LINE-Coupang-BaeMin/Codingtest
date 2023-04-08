import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 도시분할계획 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        int[] parents = new int[N];
        for (int i = 0; i < N; i++) {
            parents[i] = i;
        }
        int[][] route = new int[M][3];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int node0 = Integer.parseInt(st.nextToken()), node1 = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            route[i][0] = node0 - 1;
            route[i][1] = node1 - 1;
            route[i][2] = cost;
        }
        Arrays.sort(route, (o1, o2) -> Integer.compare(o1[2], o2[2]));
        int answer = 0;
        int cnt = 0;
        for (int i = 0; i < M; i++) {
            if (union(parents, route[i][0], route[i][1])) {
                answer += route[i][2];
                cnt += 1;
            }
            if (cnt == N - 2) {
                break;
            }
        }
        System.out.println(answer);
    }

    public static boolean union(int[] parents, int node0, int node1) {
        int x = find(parents, node0);
        int y = find(parents, node1);
        if (x == y) {
            return false;
        }
        if (x > y) {
            parents[x] = y;
        } else {
            parents[y] = x;
        }
        return true;
    }

    public static int find(int[] parents, int node) {
        if (parents[node] == node) {
            return node;
        }
        return parents[node] = find(parents, parents[node]);
    }
}