import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 회문 {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            System.out.println(check(s, 0, s.length()-1, false));
        }
    }

    public static int check(String s, int start, int last, boolean pseudo) {
        for (int i = start, j = last; i < j; i++, j--) {
//            System.out.println(i + " " + j);
            // i == j 면 홀수 case 체크 안해도됨
            // i > j 되면 짝수 case 여까지 갔으면 끝내도 됨
            if (s.charAt(i) != s.charAt(j)) {
                if (pseudo) {
                    return 2;
                } else {
                    return Math.min(check(s, i + 1, j, true), check(s, i, j - 1, true));
                }
            }
        }
        if (pseudo){
            return 1;
        }
        return 0;
    }
}
