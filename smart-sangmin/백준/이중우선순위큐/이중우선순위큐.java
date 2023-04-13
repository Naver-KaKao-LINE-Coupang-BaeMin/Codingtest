import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 이중우선순위큐 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            int k = Integer.parseInt(br.readLine());
            PriorityQueue<Token> MAX = new PriorityQueue<>(new Comparator<Token>() {
                @Override
                public int compare(Token o1, Token o2) {
                    return Integer.compare(o2.num, o1.num);
                }
            });
            PriorityQueue<Token> MIN = new PriorityQueue<>(new Comparator<Token>() {
                @Override
                public int compare(Token o1, Token o2) {
                    return Integer.compare(o1.num, o2.num);
                }
            });
            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                String comm = st.nextToken();
                int num = Integer.parseInt(st.nextToken());
                if (comm.equals("I")) {
                    Token token = new Token(i, num);
                    MAX.add(token);
                    MIN.add(token);
                } else {
                    if (num == -1) {
                        while (MIN.size() != 0 && MIN.peek().isDelete) {
                            MIN.poll();
                        }
                        if (MIN.size() != 0) {
                            Token token = MIN.poll();
                            token.isDelete = true;
                        }
                    } else {
                        while (MAX.size() != 0 && MAX.peek().isDelete) {
                            MAX.poll();
                        }
                        if (MAX.size() != 0) {
                            Token token = MAX.poll();
                            token.isDelete = true;
                        }
                    }
                }
            }
            while (MAX.size() != 0 && MAX.peek().isDelete) {
                MAX.poll();
            }
            while (MIN.size() != 0 && MIN.peek().isDelete) {
                MIN.poll();
            }
            if (MIN.size() == 0 || MAX.size() == 0) {
                sb.append("EMPTY\n");
            } else {
                sb.append(MAX.peek().num).append(" ").append(MIN.peek().num).append("\n");
            }
        }
        System.out.println(sb);
    }
}

class Token {
    int idx;
    int num;
    boolean isDelete;

    public Token(int idx, int num) {
        this.idx = idx;
        this.num = num;
        isDelete = false;
    }
}