import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ1074_Z {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int r = Integer.parseInt(stringTokenizer.nextToken());
        int c = Integer.parseInt(stringTokenizer.nextToken());

        int answer = 0;
        int x = 0;
        int y = 0;

        while (n > 0) {
            n -= 1;
            int width = (int) Math.pow(2, n);
            int area = width * width;

            boolean isLeft = true;
            boolean isUp = true;
            if (x + width <= c) {
                isLeft = false;
                x += width;
            }

            if (y + width <= r) {
                isUp = false;
                y += width;
            }

            if (isLeft && isUp) {
                answer += 0 * area;
            } else if (isLeft && !isUp) {
                answer += 2 * area;
            } else if (!isLeft && isUp) {
                answer += 1 * area;
            } else {
                answer += 3 * area;
            }
        }

        System.out.println(answer);
    }
}
