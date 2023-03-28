import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ17609_회문_re {
    static final int PALINDROME = 0;
    static final int PSEUDO_PALINDROME = 1;
    static final int NOTHING = 2;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();


        for (int i = 0; i < n; i++) {
            String string = br.readLine();
            sb.append(isPalindrome(string, 0, string.length() - 1)).append("\n");

        }

        System.out.println(sb);
    }

    private static int isPalindrome(String string, int start, int end) {
        boolean isP = true;

        while (start < end) {
            if (string.charAt(start) != string.charAt(end)) {
                isP = false;

                if (string.charAt(start) == string.charAt(end - 1)) {
                    if (isPalindrome(string, start, end - 1) == PALINDROME) {
                        return PSEUDO_PALINDROME;
                    }
                }

                if (string.charAt(start + 1) == string.charAt(end)) {
                    if (isPalindrome(string, start + 1, end) == PALINDROME) {
                        return PSEUDO_PALINDROME;
                    }
                }

                return NOTHING;

            }

            start += 1;
            end -= 1;
        }

        if (isP) {
            return PALINDROME;
        } else {
            return PSEUDO_PALINDROME;
        }

    }
}
