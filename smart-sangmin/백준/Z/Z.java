import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Z {
    static int N;
    static int r, c;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        System.out.println(Z(N, r, c));
    }

    public static int Z(int n, int row, int col) {
        if (n == 1) {
            if (row == 0 && col == 0) {
                return 0;
            }
            if (row == 0 && col == 1) {
                return 1;
            }
            if (row == 1 && col == 0) {
                return 2;
            }
            if (row == 1 && col == 1) {
                return 3;
            }
        }
        int x = (int) Math.pow(2, n);
        int half = x / 2;
        int p = (int) Math.pow(4, n - 1);

        if (row < half && col < half) { // 1사분면
            return Z(n - 1, row, col);
        } else if (row < half) {
            return p + Z(n - 1, row, col - half);
        } else if (col < half) {
            return p * 2 + Z(n - 1, row - half, col);
        } else {
            return p * 3 + Z(n - 1, row - half, col - half);
        }
    }

}