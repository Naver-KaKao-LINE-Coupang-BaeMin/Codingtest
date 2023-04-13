import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 문제추천시스템V1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        HashMap<Integer, Problem> map = new HashMap<>();
        PriorityQueue<Problem> MAX = new PriorityQueue<>((o1, o2) -> o2.level != o1.level ? o2.level - o1.level : o2.number - o1.number);
        PriorityQueue<Problem> MIN = new PriorityQueue<>((o2, o1) -> o2.level != o1.level ? o2.level - o1.level : o2.number - o1.number);
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            add(st, map, MAX, MIN);
        }
        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            String com = st.nextToken();
            switch (com) {
                case "add": {
                    add(st, map, MAX, MIN);
                    break;
                }
                case "recommend":
                    int x = Integer.parseInt(st.nextToken());
                    if (x == -1) {
                        while (MIN.peek().deleted) {
                            MIN.poll();
                        }
                        Problem p = MIN.peek();
                        System.out.println(p.number);
                    } else {
                        while (MAX.peek().deleted) {
                            MAX.poll();
                        }
                        Problem p = MAX.peek();
                        System.out.println(p.number);
                    }
                    break;
                case "solved": {
                    int P = Integer.parseInt(st.nextToken());
                    map.get(P).deleted = true;
                    map.remove(P);
                    break;
                }
            }
        }
    }

    private static void add(StringTokenizer st, HashMap<Integer, Problem> map, PriorityQueue<Problem> MAX, PriorityQueue<Problem> MIN) {
        int P = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        Problem problem = new Problem(P, L);
        MAX.add(problem);
        MIN.add(problem);
        map.put(P, problem);
    }
}

class Problem {
    int number;
    int level;
    boolean deleted;

    public Problem(int number, int level) {
        this.number = number;
        this.level = level;
        deleted = false;
    }
}
