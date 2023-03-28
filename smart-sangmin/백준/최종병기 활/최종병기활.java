import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 최종병기활 {
    static int N; // 고무줄 길이
    static int M; // 홈의 개수
    static int K; // 고무줄 겹치는 수
    static int[] X; // 홈 목록


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        X = new int[M];
        for (int i = 0; i < M; i++) {
            X[i] = Integer.parseInt(br.readLine());
        }

        if (K == 1) {
            System.out.println(N);
        } else {
            int start = 0;
            int end = N / K;

            while (start <= end) {
                int mid = (start + end) / 2;
                boolean flag = false;
                for (int idx = 0; idx < M; idx++) {
                    if (bound(mid, idx)) {
                        flag = true;
                        break;
                    }
                }
                if (flag) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
            System.out.println(end);
        }
    }

    public static boolean bound(int mid, int flag) {
        int cnt = 0;
        int cur = flag;
        int next = (cur + 1) % M;
        while (next != flag) {
            if (calc(cur, next) >= mid) {
                cnt++;
                cur = next;
                if (cnt >= K-1) {
                    if (calc(cur, flag) >= mid) {
                        return true;
                    }
                    return false;
                }
            }
            next = (next + 1) % M;
        }
        return false;
    }

    public static int calc(int i, int j) {
        return (X[j] - X[i] + N) % N;
    }
}
//19 4 3
//0
//7
//11
//13

//20 3 3
//2
//4
//6