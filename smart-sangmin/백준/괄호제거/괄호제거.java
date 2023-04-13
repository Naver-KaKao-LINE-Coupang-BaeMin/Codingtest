import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 괄호제거 {
    static ArrayList<String> com = new ArrayList<>();
    static ArrayList<Integer[]> brackets = new ArrayList<>();
    static TreeSet<String> answer = new TreeSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        getGOGO(s);
        combination("", 0);
        Collections.sort(com);

        for (String candi : com) {
            if (candi.equals("")) {
                continue;
            }
            List<Integer> concat = new ArrayList<>();
            for (char c : candi.toCharArray()) {
                concat.addAll(new ArrayList<>(Arrays.asList(brackets.get(c - '0'))));
            }
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < s.length(); i++) {
                if (concat.contains(i)) {
                    continue;
                }
                sb.append(s.charAt(i));
            }
            answer.add(sb.toString());
        }

        for (String ans : answer) {
            System.out.println(ans);
        }
    }

    public static void getGOGO(String s) {
        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                st.add(i);
            }
            if (s.charAt(i) == ')') {
                brackets.add(new Integer[]{st.pop(), i});
            }
        }
    }

    public static void combination(String cand, int idx) {
        if (brackets.size() <= idx) {
            com.add(cand);
            return;
        }
        combination(cand, idx + 1);
        combination(cand + idx, idx + 1);
    }
}