//3 3
//1 2 1
//2 3 2
//1 3 3

//3 3
//        1 2 1
//        2 3 2
//        1 2 -100

//5 5
//1 4 3
//2 3 3
//4 3 5
//2 1 6
//4 5 9


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 최소스패닝트리 {
    static int[] check;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken()), E = Integer.parseInt(st.nextToken());
        int[][] arr = new int[E][3];
        check = new int[V + 1];
        for (int i = 1; i < V + 1; i++) {
            check[i] = i;
        }
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            arr[i] = new int[]{s, e, w};
        }
        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[2] - o2[2];
            }
        });
//        for (int[] ar : arr) {
//            System.out.println(Arrays.toString(ar));
//        }

        int answer = 0;
        for (int i = 0; i < E; i++) {
            int[] shortest = arr[i];
            if (find(check[shortest[0]]) != find(check[shortest[1]])) {
                union(shortest[0], shortest[1]);
                answer += shortest[2];
            }
        }
        System.out.println(answer);
    }

    public static int find(int x) {
        if (x == check[x]) {
            return x;
        }
        return check[x] = find(check[x]);
    }

    public static void union(int x, int y) {
        int getX = find(x);
        int getY = find(y);
        if (getX > getY) {
            check[getX] = getY;
        } else {
            check[getY] = getX;
        }
    }
}
