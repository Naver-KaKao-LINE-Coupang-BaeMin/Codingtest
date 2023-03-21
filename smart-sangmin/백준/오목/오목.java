import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 오목 {
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        board = new int[19][19];
        for (int i = 0; i < 19; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 19; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int answer = 0;
        int[] coor = new int[2];
        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 19; j++) {
                if (board[j][i] != 0 && bingo(j, i)) {
                    answer = board[j][i];
                    coor = new int[]{j + 1, i + 1};
                    System.out.println(answer);
                    if (answer != 0) {
                        System.out.println(coor[0] + " " + coor[1]);
                    }
                    System.exit(0);
                }
            }
        }
        System.out.println(answer);
    }

    public static boolean bingo(int y, int x) {
        int[][] go = {{0, 1}, {1, 0}, {1, 1}, {-1, 1}};
        for (int[] g : go) {
            if (0 <= y - g[0] && y - g[0] < 19 && 0 <= x - g[1] && x - g[1] < 19 && board[y - g[0]][x - g[1]] == board[y][x]) {
                continue;
            }
            if (gogo(y, x, g[0], g[1], 1)) {
                return true;
            }
        }
        return false;
    }

    public static boolean gogo(int y, int x, int a, int b, int cnt) {
        if (cnt > 5) {
            return false;
        }

        if (0 <= y + a && y + a < 19 && 0 <= x + b && x + b < 19) {
            if (board[y][x] == board[y + a][x + b]) {
                return gogo(y + a, x + b, a, b, cnt + 1);
            }
        }
        return cnt == 5;
    }
}