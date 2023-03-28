import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 넴모넴모 {
    static int N, M;
    static int[] board;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N * M];
        cntCase(0);
        System.out.println(answer);
    }

    public static void cntCase(int prev) {
        int row = prev / M;
        int col = prev % M;

        if (row >= 1 && col >= 1 && checkNemo(row, col)) {
            return;
        }
        answer++;
        for (int i = prev; i < N * M; i++) {
            if (board[i] == 0) {
                board[i] = 1;
                cntCase(i);
                board[i] = 0;
            }
        }
    }

    public static boolean checkNemo(int row, int col) {
        return board[(row - 1) * M + (col - 1)] == 1 &&
                board[(row - 1) * M + (col)] == 1 &&
                board[(row) * M + (col - 1)] == 1 &&
                board[(row) * M + (col)] == 1;
    }
}
