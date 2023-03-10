import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ1747_소수팰린드롬 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        while (true) {
            if (isPelindrom(n) && isPrime(n)) {
                System.out.println(n);
                break;
            } else {
                n += 1;
            }
        }
    }

    private static boolean isPrime(int number) {
        int root = (int) Math.sqrt(number);
        for (int i = 2; i <= root; i++) {
            if (number % i == 0) {
                return false;
            }
        }

        if (number == 1) {
            return false;
        }

        return true;
    }

    private static boolean isPelindrom(int number) {
        String string = number + "";
        int length = string.length();
        int left = 0;
        int right = length - 1;
        while (left < right) {
            if (string.charAt(left) != string.charAt(right)) {
                return false;
            }
            left += 1;
            right -= 1;
        }

        return true;
    }
}
