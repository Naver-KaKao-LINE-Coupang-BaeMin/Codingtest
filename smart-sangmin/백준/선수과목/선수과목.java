import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 선수과목 {
    static int N, M;
    static ArrayList<Integer>[] subjects;
    static int[] answer;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        subjects = new ArrayList[N + 1];
        answer = new int[N + 1];
        Arrays.fill(answer, 1);

        for (int i = 1; i <= N; i++) {
            subjects[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int pre = Integer.parseInt(st.nextToken()), post = Integer.parseInt(st.nextToken());
            subjects[post].add(pre);
        }
        for (int i = 1; i <= N; i++) {
            if (!subjects[i].isEmpty()) {
                int MAX = 0;
                for (int a : subjects[i]) {
                    MAX = Math.max(answer[a] + 1,  MAX);
                }
                answer[i] = MAX;
            }
        }
        for (int i = 1; i <= N; i++) {
            System.out.print(answer[i] + " ");
        }
    }
}










