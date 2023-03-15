import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ20922_겹치는건싫어 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int k = Integer.parseInt(stringTokenizer.nextToken());
        int end = 0;
        int answer = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        stringTokenizer = new StringTokenizer(br.readLine());

        int[] array = new int[n];
        for (int i = 0; i < n; i++) {
            int current = Integer.parseInt(stringTokenizer.nextToken());
            array[i] = current;
            map.put(current, 0);
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            int current = array[i];
            queue.add(current);

            if (map.get(current) + 1 > k) {
                while (current != queue.peek()) {
                    int temp = queue.poll();
                    map.put(temp, map.get(temp) - 1);
                }
                queue.poll();
            } else {
                map.put(array[i], map.get(array[i]) + 1);
                answer = Math.max(answer, queue.size());
            }
        }

        System.out.println(answer);

    }
}
