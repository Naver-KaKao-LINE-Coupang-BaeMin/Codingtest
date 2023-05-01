import java.io.*;
import java.util.*;

public class 나무위의빗물 {
    static ArrayList<Integer>[] tree;
    static int N, W;
    static int cntLeaf = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        tree = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            tree[i] = new ArrayList<>();
        }
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            tree[node1].add(node2);
            tree[node2].add(node1);
        }


        for (int i = 2; i <= N; i++) {
            if (tree[i].size() == 1)
                cntLeaf++;
        }
        System.out.printf("%.6f", W / (double) cntLeaf);
    }

    public static void count(int parent, int cur) {
        if (cur != 1 && tree[cur].size() == 1) {
            cntLeaf++;
            return;
        }
        for (Integer n : tree[cur]) {
            if (n == parent) {
                continue;
            }
            count(cur, n);
        }
    }
}

