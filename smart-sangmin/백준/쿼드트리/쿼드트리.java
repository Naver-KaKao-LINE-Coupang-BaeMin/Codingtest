import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 쿼드트리 {
    static int N;
    static char[][] board;
    static StringBuilder ans = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new char[N][N];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                board[i][j] = line.charAt(j);
            }
        }
        dc(N, 0, 0);
        System.out.println(ans);
    }


    public static void dc(int n, int row, int col) {
        char flag = board[row][col];
        for (int i = row; i < row + n; i++) {
            for (int j = col; j < col + n; j++) {
                if (flag != board[i][j]) {
                    int half = n / 2;
                    ans.append("(");
                    dc(half, row, col);
                    dc(half, row, col + half);
                    dc(half, row + half, col);
                    dc(half, row + half, col + half);
                    ans.append(")");
                    return;
                }
            }
        }
        ans.append(flag);
    }
}
