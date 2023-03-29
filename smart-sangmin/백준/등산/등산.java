import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 등산 {
    static int N, M, T, D;
    static int[][] map;
    static int top = -1;
    static int[] topCoor;
    static int[][] up;
    static int[][] down;
    static int[][] directions = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 최대 차이 T
        // 낮은 곳 or 같은 곳 1초
        // 높은 곳 차이^2
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        HashMap<Integer, Integer> table = new HashMap<Integer, Integer>();
        for (int i = 0; i < 26; i++) {
            table.put('A' + i, i);
        }
        for (int i = 26; i < 52; i++) {
            table.put('a' + i - 26, i);
        }
        map = new int[N][M];
        up = new int[N][M];
        down = new int[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = table.get((int) line.charAt(j));
            }
        }
        goTop();
        up[0][0] = 0;
//        pprint(up);

        goHotel();
        down[0][0] = 0;
//        pprint(down);

        int top = map[0][0];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int sum = up[i][j] + down[i][j];
                if (0 < sum && sum <= D && top < map[i][j]) {
                    top = map[i][j];
                }
            }
        }
        System.out.println(top);
    }

    static void goTop() {
        PriorityQueue<int[]> q = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[2] - o2[2];
            }
        });
        q.add(new int[]{0, 0, 0});
        while (!q.isEmpty()) {
            int[] coor = q.poll();
            int y = coor[0], x = coor[1], time = coor[2];
            if (map[y][x] > top) {
                top = map[y][x];
                topCoor = new int[]{y, x};
            }
            for (int[] direction : directions) {
                int ty = direction[0] + y, tx = direction[1] + x;
                if (0 <= ty && ty < N && 0 <= tx && tx < M && Math.abs(map[ty][tx] - map[y][x]) <= T) {
                    int diffPow = Math.abs(map[ty][tx] - map[y][x]) * Math.abs(map[ty][tx] - map[y][x]);
                    int need = (map[ty][tx] <= map[y][x] ? 1 : diffPow);
                    if (up[ty][tx] == 0 || up[ty][tx] > time + need) {
                        up[ty][tx] = time + need;
                        q.add(new int[]{ty, tx, time + need});
                    }
                }
            }
        }
    }

    static int goHotel() {
        PriorityQueue<int[]> q = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[2] - o2[2];
            }
        });
        q.add(new int[]{0, 0, 0});
        while (!q.isEmpty()) {
            int[] coor = q.poll();
            int y = coor[0], x = coor[1], time = coor[2];
            for (int[] direction : directions) {
                int ty = direction[0] + y, tx = direction[1] + x;
                if (0 <= ty && ty < N && 0 <= tx && tx < M && Math.abs(map[ty][tx] - map[y][x]) <= T) {
                    int diffPow = Math.abs(map[ty][tx] - map[y][x]) * Math.abs(map[ty][tx] - map[y][x]);
                    int need = (map[ty][tx] >= map[y][x] ? 1 : diffPow);
                    if (down[ty][tx] == 0 || down[ty][tx] > time + need) {
                        down[ty][tx] = time + need;
                        q.add(new int[]{ty, tx, time + need});
                    }
                }
            }
        }
        return 0;
    }


    static void pprint(int[][] s) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(s[i][j] + " ");
            }
            System.out.println();
        }
    }
}
