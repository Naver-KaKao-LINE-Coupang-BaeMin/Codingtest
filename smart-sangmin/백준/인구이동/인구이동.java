import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 인구이동 {
    static int N;
    static int L;
    static int R;
    static int[][] maps;
    static int[][] direction = new int[][]{{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        maps = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = 0;
        int flag = 1;
        while (true) {
            flag = -1;
            boolean[][] visited = new boolean[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (!visited[i][j]) {
                        flag = Math.max(checkOpen(i, j, visited), flag);
                    }
                }
            }
            if (flag == -1) {
                break;
            }
            answer += 1;
        }
        System.out.println(answer);
    }

    // bfs 다같이 오픈하면 안됨
    public static int checkOpen(int a, int b, boolean[][] visited) {
        ArrayList<int[]> openList = new ArrayList<>();
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{a, b});
        while (!queue.isEmpty()) {
            int[] c = queue.poll();
            int i = c[0];
            int j = c[1];
            for (int[] d : direction) {
                int y = i + d[0];
                int x = j + d[1];
                if (0 <= y && y < N && 0 <= x && x < N) {
                    if (checkRange(maps[y][x], maps[i][j]) && !visited[y][x]) {
                        queue.add(new int[]{y, x});
                        openList.add(new int[]{y, x});
                        visited[y][x] = true;
                    }
                }
            }
        }
//        for (int[] coor : openList) {
//            System.out.println(coor[0] + " " + coor[1]);
//        }
        int sum = 0;
        int size = openList.size();
        if (size == 0) {
            return -1;
        }
        for (int[] coor : openList) {
            sum += maps[coor[0]][coor[1]];
        }
        int population = (int) Math.floor(sum / (double) size);
        for (int[] coor : openList) {
            maps[coor[0]][coor[1]] = population;
        }

        return 1;
    }

    public static boolean checkRange(int a, int b) {
        return L <= Math.abs(a - b) && Math.abs(a - b) <= R;
    }

    public static void printMaps() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(maps[i][j] + " ");
            }
            System.out.println();
        }
    }
}
