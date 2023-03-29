import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 문자열게임2 {
    static int T;
    static int MAX;
    static int MIN;
    static int K;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            MAX = -1;
            MIN = Integer.MAX_VALUE;
            String W = br.readLine(); //소문자만
            K = Integer.parseInt(br.readLine());
            int[] alpha = new int[26];
            for (int j = 0; j < W.length(); j++) {
                alpha[W.charAt(j) - 'a']++;
                // 여기서 바로 check?
            }
            for (int j = 0; j < W.length(); j++) {
                if (alpha[W.charAt(j) - 'a'] >= K) {
                    check(W, j);
                }
            }
            if (MAX == -1) {
                System.out.println(-1);
            } else {
                System.out.println(MIN + " " + MAX);
            }
        }
    }

    public static void check(String s, int start) {
        char flag = s.charAt(start);
        int cnt = 0;
        for (int i = start; i < s.length(); i++) {
            if (s.charAt(i) == flag) {
                cnt++;
            }
            if (cnt == K) {
//                System.out.println(start + " " + i);
                MAX = Math.max(MAX, i - start + 1);
                MIN = Math.min(MIN, i - start + 1);
                break; // ?
            }
        }
    }
}
