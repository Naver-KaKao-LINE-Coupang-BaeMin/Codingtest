import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ13164_행복유치원 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int k = Integer.parseInt(stringTokenizer.nextToken());
        int[] kids = new int[n];
        stringTokenizer = new StringTokenizer(br.readLine());
        int before = Integer.parseInt(stringTokenizer.nextToken());

        for (int i = 1; i < n; i++) {
            int current = Integer.parseInt(stringTokenizer.nextToken());
            kids[i] = current - before;
            before = current;
        }

        Arrays.sort(kids);

        int answer = 0;

        for (int i = 0; i < n - k + 1; i++) {
            answer += kids[i];
        }

        System.out.println(answer);
    }
}
