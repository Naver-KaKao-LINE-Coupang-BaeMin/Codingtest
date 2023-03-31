import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ25168_게으른아리 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        int vaccine = Integer.parseInt(stringTokenizer.nextToken());
        int condition = Integer.parseInt(stringTokenizer.nextToken());

        int[] array = new int[vaccine + 1];
        int[] timeArray = new int[vaccine + 1];
        ArrayList<Integer>[] relationArray = new ArrayList[vaccine + 1];

        for (int i = 1; i <= vaccine; i++) {
            relationArray[i] = new ArrayList<>();
        }

        for (int i = 0; i < condition; i++) {
            stringTokenizer = new StringTokenizer(br.readLine());
            int before = Integer.parseInt(stringTokenizer.nextToken());
            int after = Integer.parseInt(stringTokenizer.nextToken());
            int duration = Integer.parseInt(stringTokenizer.nextToken());

            relationArray[before].add(after);
            if (duration >= 7) {
                duration += 1;
            }
            relationArray[before].add(duration);
            array[after] += 1;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= vaccine; i++) {
            if (array[i] == 0) {
                queue.add(i);
                timeArray[i] = 1;
            }
        }

        int max = 0;
        while (!queue.isEmpty()) {
            int index = queue.poll();
            for (int i = 0; i < relationArray[index].size() - 1; i += 2) {
                int after = relationArray[index].get(i);
                int duration = relationArray[index].get(i + 1);
                timeArray[after] = Math.max(timeArray[after], timeArray[index] + duration);
                max = Math.max(timeArray[after], max);

                array[after] -= 1;
                if (array[after] == 0) {
                    queue.add(after);
                }
            }
        }

        System.out.println(max);
    }
}
