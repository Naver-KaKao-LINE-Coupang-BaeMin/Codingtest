import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 가희와자원놀이 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        Person[] people = new Person[N];
        for (int i = 0; i < N; i++) {
            people[i] = new Person();
        }

        int T = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] turn = new int[T];
        for (int i = 0; i < T; i++) {
            turn[i] = Integer.parseInt(st.nextToken());
        }

        Queue<Card> q = new LinkedList<>();
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int number = Integer.parseInt(st.nextToken());
            String command = st.nextToken();
            Card card;
            if (command.equals("acquire") || command.equals("release")) {
                int n = Integer.parseInt(st.nextToken());
                card = new Card(number, command, n);
            } else {
                card = new Card(number, command);
            }
            q.add(card);
        }

        StringBuilder sb = new StringBuilder();
        HashSet<Integer> took = new HashSet<>(); // 누가 가져간 자원

        for (int i = 0; i < T; i++) {
            Card card;
            int p = turn[i] - 1;
            if (people[p].operationCard == null) {
                card = q.poll();
            } else {
                card = people[p].operationCard;
            }

            if (card.command.equals("acquire")) {
                if (!took.contains(card.n)) {
                    if (people[p].operationCard != null) {
                        people[p].operationCard = null;
                    }
                    took.add(card.n);
                } else {
                    people[p].operationCard = card;
                }
            } else if (card.command.equals("release")) {
                took.remove((Integer) card.n);
            }
            sb.append(card.number).append("\n");
        }
        System.out.println(sb);
    }
}

class Person {
    Card operationCard;

    public Person() {
        this.operationCard = null;
    }
}

class Card {
    int number;
    String command;
    int n; // acq, rea 일 때

    public Card(int number, String command) {
        this.number = number;
        this.command = command;
    }

    public Card(int number, String command, int n) {
        this.number = number;
        this.command = command;
        this.n = n;
    }
}
