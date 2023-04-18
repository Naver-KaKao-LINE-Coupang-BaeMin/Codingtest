import java.io.*;
import java.util.*;

public class 트리의지름 {
    static int N;
    static List<Integer[]>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        graph = new ArrayList[N + 1];
        for (int i = 1; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph[a].add(new Integer[]{b, w});
        }
        // for (List<Integer[]> l : Arrays.copyOfRange(graph, 1, graph.length)) {
        //     for (Integer[] a : l){
        //         System.out.print(Arrays.toString(a) + " ");
        //     }
        //     System.out.println();
        // }
        int answer = 0;

        if (N == 2){
            answer = graph[1].get(0)[1];
        }
        else{
            for (int i = 1; i < N + 1; i++) {
                List<Integer> temp = new ArrayList<>();
                for (Integer[] part : graph[i]) {
                    int next = part[0];
                    int length = part[1];
                    temp.add(getLength(next, length));
                }
                if (temp.size() == 0){
                    continue;
                }
                if (temp.size() == 1){
                    answer = Math.max(temp.get(0), answer);
                }
                else {
                    temp.sort(Collections.reverseOrder());
                    answer = Math.max(temp.get(0) + temp.get(1), answer);
                }
            }
        }
        System.out.println(answer);
    }

    public static int getLength(int node, int totLength) {
        if (graph[node].size() == 0){
            return totLength;
        }
        int MAX = 0;
        for (Integer[] edge : graph[node]) {
            int next = edge[0];
            int length = edge[1];
            MAX = Math.max(getLength(next, totLength + length), MAX);
        }
        return MAX;
    }
}










