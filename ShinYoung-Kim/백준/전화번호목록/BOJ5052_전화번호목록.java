import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashSet;

public class BOJ5052_전화번호목록 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            String[] stringArray = new String[n];
            for (int j = 0; j < n; j++) {
                stringArray[j] = br.readLine();
            }

            Arrays.sort(stringArray);

            HashSet<String> set = new HashSet();
            boolean isStartsWith = false;
            for (int j = 0; j < n; j++) {
                String string = stringArray[j];
                /*
                for (String savedString : set) {
                    if (string.startsWith(savedString)) {
                        isStartsWith = true;
                        break;
                    }
                }

                 */

                int length = string.length();
                for (int k = 0; k < length; k++) {
                    if (set.contains(string.substring(0, k))) {
                        isStartsWith = true;
                        break;
                    }
                }

                if (isStartsWith) {
                    break;
                } else {
                    set.add(string);
                }
            }

            if (isStartsWith) {
                sb.append("NO").append("\n");
            } else {
                sb.append("YES").append("\n");
            }
        }

        bw.write(String.valueOf(sb));
        bw.flush();
        bw.close();
    }
}
