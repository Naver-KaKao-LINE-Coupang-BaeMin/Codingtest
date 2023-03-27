import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class BOJ2015_수들의합4_re {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int k = Integer.parseInt(stringTokenizer.nextToken());

        stringTokenizer = new StringTokenizer(br.readLine());
        int[] array = new int[n];
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            array[i] = Integer.parseInt(stringTokenizer.nextToken());
            if (i != 0) {
                array[i] += array[i - 1];
            }

            if (map.containsKey(array[i])) {
                map.put(array[i], map.get(array[i]) + 1);
            } else {
                map.put(array[i], 1);
            }
        }

        long count = 0;

        for (int i = 0; i < n; i++) {
            if (array[i] == k) {
                count += (long) 1;
            }

            if (k != 0) {
                if (map.containsKey(array[i] + k)) {
                    count += (long) map.get(array[i] + k);
                }

                /*
                if (map.containsKey(array[i] - k)) {
                    count += (long) map.get(array[i] - k);
                }

                 */
            } else {
                if (map.containsKey(array[i])) {
                    count += (long) map.get(array[i]) - 1;
                }
            }

            map.put(array[i], map.get(array[i]) - 1);
        }

        System.out.println((long) count);
    }
}
