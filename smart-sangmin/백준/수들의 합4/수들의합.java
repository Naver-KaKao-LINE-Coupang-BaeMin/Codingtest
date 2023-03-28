import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.StringTokenizer;

//4 0
//2 -2 2 -2
public class 수들의합 {
    static int N;
    static int K;
    static int[] nums;
    static int[] sums;
    static long cnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        nums = new int[N];
        sums = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
            sums[i] = (i - 1 >= 0 ? sums[i - 1] : 0) + nums[i];
        }
        count();
        System.out.println(cnt);
    }

    public static void count() {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        for (int i = 0; i < N; i++) {
            cnt += map.getOrDefault(sums[i] - K, 0);
            map.put(sums[i], map.getOrDefault(sums[i], 0) + 1);
//            for (int j = 0; j < i; j++) {
//                if (sums[j] == sums[j] - K) {
////                    System.out.println(i + " " + j);
//                    cnt++;
//                }
//            }
        }
    }
}