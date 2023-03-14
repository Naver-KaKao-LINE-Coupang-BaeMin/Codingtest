import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ13422_도둑 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(stringTokenizer.nextToken());
            int m = Integer.parseInt(stringTokenizer.nextToken());
            int k = Integer.parseInt(stringTokenizer.nextToken());

            int[] houseArray = new int[n + m - 1];
            stringTokenizer = new StringTokenizer(br.readLine());

            for (int j = 0; j < n; j++) {
                int current = Integer.parseInt(stringTokenizer.nextToken());
                if (j < m - 1) {
                    houseArray[n + j] = current;
                }
                houseArray[j] = current;
            }

            int sum = 0;
            for (int j = 0; j < m; j++) {
                sum += houseArray[j];
            }

            int answer = sum < k? 1 : 0;

            for (int start = 1; start < n; start++) {
                sum -= (houseArray[start - 1] - houseArray[start + m - 1]);
                if (sum < k) {
                    answer += 1;
                }
            }

            if (n == m) {
                answer /= m;
            }
            sb.append(answer).append("\n");
        }
        System.out.println(sb);
    }
}
