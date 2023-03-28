import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Queue;

public class BOJ20437_문자열게임 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < t; i++) {
            String string = br.readLine();
            int number = Integer.parseInt(br.readLine());
            int length = string.length();
            ArrayList<Integer>[] alphabets = new ArrayList[26];
            for (int j = 0; j < 26; j++) {
                alphabets[j] = new ArrayList<Integer>();
            }

            int min = Integer.MAX_VALUE;
            int max = 0;

            HashMap<Character, Queue<Integer>> map = new HashMap<>();
            for (int j = 0; j < length; j++) {
                char current = string.charAt(j);
                alphabets[current - 'a'].add(j);
            }

            for (int j = 0; j < 26; j++) {
                int size = alphabets[j].size();
                if (size >= number) {

                    for (int k = 0; k < size; k++) {
                        if (k + number - 1 >= size) {
                            break;
                        }
                        min = Math.min(alphabets[j].get(k + number - 1) - alphabets[j].get(k) + 1, min);
                        max = Math.max(max, alphabets[j].get(k + number - 1) - alphabets[j].get(k) + 1);
                    }
                }
            }

            if (max > 0) {
                sb.append(min).append(" ").append(max).append("\n");
            } else {
                sb.append(-1).append("\n");
            }
        }

        System.out.println(sb);
    }
}
