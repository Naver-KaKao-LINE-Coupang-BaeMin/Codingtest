import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[] bridge;
    static int answer = 0;
    static long[] dp;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());

        // i$번째 돌에서 j(i < j)번째 돌로 이동할 때 (j - i) × (1 +  |A{i} - A{j}|) 만큼 힘을 쓴다.
        st = new StringTokenizer(br.readLine());
        bridge = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            bridge[i] = Integer.parseInt(st.nextToken());
        }

        dp = new long[N + 1];
        Arrays.fill(dp, Long.MAX_VALUE);
        dp[0] = 0;
        dp[1] = 0;
        for (int i = 2; i <= N; i++) {
            cross(i);
        }
//        for (int a : dp){
//            System.out.print(a + " ");
//        }
        System.out.println(dp[N]);
    }

    public static long calc(int i, int j) {
        return (long) (j - i) * (1 + Math.abs(bridge[i] - bridge[j]));
    }

    public static void cross(int idx) {
        for (int i = 1; i < idx; i++) {
            dp[idx] = Math.min(Math.max(dp[i], calc(i, idx)), dp[idx]);
        }
    }
}