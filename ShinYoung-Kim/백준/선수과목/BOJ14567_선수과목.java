import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class BOJ14567_선수과목 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        int classNumber = Integer.parseInt(stringTokenizer.nextToken());
        int conditionNumber = Integer.parseInt(stringTokenizer.nextToken());

        PriorityQueue<Integer>[] relation = new PriorityQueue[classNumber + 1];
        for (int i = 1; i <= classNumber; i++) {
            relation[i] = new PriorityQueue<>();
        }
        int[] array = new int[classNumber + 1];
        Arrays.fill(array, 1);

        for (int i = 0; i < conditionNumber; i++) {
            stringTokenizer = new StringTokenizer(br.readLine());
            int before = Integer.parseInt(stringTokenizer.nextToken());
            int after = Integer.parseInt(stringTokenizer.nextToken());
            relation[after].add(before);
            //array[after] = Math.max(array[before] + 1, array[after]);

            /*
            if (!relation[after].isEmpty()) {
                for (int afterClass : relation[after]) {
                    array[]
                }
            }

             */
        }

        for (int i = 1; i <= classNumber; i++) {
            if (!relation[i].isEmpty()) {
                int max = 0;
                for (int beforeClass : relation[i]) {
                    max = Math.max(array[beforeClass], max);
                }
                array[i] = max + 1;
            }
        }

        //System.out.println(Arrays.toString(array));

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= classNumber; i++) {
            sb.append(array[i]).append(" ");
        }
        System.out.println(sb);
    }
}
