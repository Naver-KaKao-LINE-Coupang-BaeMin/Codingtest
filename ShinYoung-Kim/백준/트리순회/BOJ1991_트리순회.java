import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class BOJ1991_트리순회 {
    static StringBuilder before = new StringBuilder();
    static StringBuilder center = new StringBuilder();
    static StringBuilder after = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[][] tree = new String[n][3];

        for (int i = 0; i < n; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                tree[i][j] = stringTokenizer.nextToken();
            }
        }

        boolean[] beforeVisited = new boolean[n];
        beforeSearch(tree, 0, beforeVisited);

        boolean[] centerVisited = new boolean[n];
        centerSearch(tree, 0, centerVisited);

        boolean[] afterVisited = new boolean[n];
        afterSearch(tree, 0);
        System.out.println(before);
        System.out.println(center);
        System.out.println(after);
    }

    private static void beforeSearch(String[][] tree, int root, boolean[] visited) {
        if (visited[root]) {
            return;
        }

        before.append(tree[root][0]);
        visited[root] = true;
        if (!tree[root][1].equals(".")) {
            beforeSearch(tree, findIndex(tree, tree[root][1]), visited);
        }

        if (!tree[root][2].equals(".")) {
            beforeSearch(tree, findIndex(tree, tree[root][2]), visited);
        }

    }

    private static void afterSearch(String[][] tree, int root) {

        if (!tree[root][1].equals(".")) {
            afterSearch(tree, findIndex(tree, tree[root][1]));
        }

        if (!tree[root][2].equals(".")) {
            afterSearch(tree, findIndex(tree, tree[root][2]));
        }

        after.append(tree[root][0]);

    }

    private static void centerSearch(String[][] tree, int root, boolean[] visited) {
        if (visited[root]) {
            return;
        }

        if (!tree[root][1].equals(".")) {
            if (!visited[findIndex(tree, tree[root][1])]) {
                centerSearch(tree, findIndex(tree, tree[root][1]), visited);
                if (!visited[findIndex(tree, tree[root][1])]) {
                    visited[findIndex(tree, tree[root][1])] = true;
                    center.append(tree[root][1]);
                }
            }
        }

        center.append(tree[root][0]);
        visited[root] = true;

        if (!tree[root][2].equals(".")) {
            if (!visited[findIndex(tree, tree[root][2])]) {
                centerSearch(tree, findIndex(tree, tree[root][2]), visited);
                if (!visited[findIndex(tree, tree[root][2])]) {
                    visited[findIndex(tree, tree[root][2])] = true;
                    center.append(tree[root][2]);
                }
            }
        }

    }

    private static int findIndex(String[][] tree, String target) {
        for (int i = 0; i < tree.length; i++) {
            if (tree[i][0].equals(target)) {
                return i;
            }
        }

        return -1;
    }
}
