import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ2560_짚신벌레 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(stringTokenizer.nextToken());
        int b = Integer.parseInt(stringTokenizer.nextToken());
        int d = Integer.parseInt(stringTokenizer.nextToken());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        ArrayList<Integer> ages = new ArrayList<>();

        for (int i = 0; i < d - 1; i++) {
            ages.add(0);
        }
        ages.add(1);
        int sum = 0;

        for (int i = 1; i <= n; i++) {
            sum += (1000 + ages.get(d - a) - ages.get(d - b)) % 1000;
            sum %= 1000;
            ages.add(sum);
            ages.remove(0);
        }

        int count = 0;
        for (int i = 0; i < d; i++) {
            count += ages.get(i) % 1000;
            count %= 1000;
        }

        System.out.println(count);
    }
}
