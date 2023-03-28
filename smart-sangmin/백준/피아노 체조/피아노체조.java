import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 피아노체조 {
    static int N;
    static int[] akbo;
    static int[] s;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        akbo = new int[N + 1];
        s = new int[N + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            akbo[i] = Integer.parseInt(st.nextToken());
            s[i] = s[i - 1];
            if (akbo[i] < akbo[i - 1]) {
                s[i]++;
            }
        }
//        for (int ss : s){
//            System.out.print(ss+" ");
//        }
        int Q = Integer.parseInt(br.readLine());
        for (int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            System.out.println(s[end] - s[start]);
        }
    }
}