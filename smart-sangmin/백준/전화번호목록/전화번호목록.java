import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class 전화번호목록 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());
            String[] numbers = new String[N];
            String answer = "YES";

            for (int i = 0; i < N; i++) {
                numbers[i] = br.readLine();
            }
            Arrays.sort(numbers);

            for (int i = 0; i < N - 1; i++) {
                if (numbers[i + 1].startsWith(numbers[i])) {
                    answer = "NO";
                    break;
                }
            }
            sb.append(answer).append("\n");
        }
        System.out.println(sb);
    }
}