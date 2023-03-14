import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class BOJ11286_절댓값힙 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0]) {
                    return o1[1] - o2[1];
                } else {
                    return o1[0] - o2[0];
                }
            }
        });

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            int current = Integer.parseInt(br.readLine());

            if (current == 0) {
                if (!pq.isEmpty()) {
                    sb.append(pq.poll()[1]).append("\n");
                } else {
                    sb.append(0).append("\n");
                }
            } else {
                pq.add(new int[]{Math.abs(current), current});
            }
        }

        System.out.println(sb);
    }
}
