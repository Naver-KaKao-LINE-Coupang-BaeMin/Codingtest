import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 웹브라우저1 {
    static int N, Q, C;
    static int cache;
    static Page[] pages;
    static Store back = new Store();
    static Page cur;
    static Store front = new Store();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        pages = new Page[N + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            pages[i + 1] = new Page(i + 1, Integer.parseInt(st.nextToken()));
        }

        for (int q = 0; q < Q; q++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            switch (command) {
                case "B":
                    backward();
                    break;
                case "F":
                    frontward();
                    break;
                case "A":
                    int num = Integer.parseInt(st.nextToken());
                    access(pages[num]);
                    break;
                case "C":
                    compress();
                    break;
            }
        }
        System.out.println(cur.number);
        printDeque(back.q);
        printDeque(front.q);
    }

    public static void printDeque(Deque<Page> d) {
        if (d.isEmpty()) {
            System.out.println(-1);
        } else {
            while (!d.isEmpty()) {
                Page page = d.pollLast();
                System.out.print(page.number + " ");
            }
            System.out.println();
        }
    }

    public static void backward() {
        if (back.isEmpty()) {
            return;
        }
        front.add(cur);
        cur = back.pop();
    }

    public static void frontward() {
        if (front.isEmpty()) {
            return;
        }
        back.add(cur);
        cur = front.pop();
    }

    public static void access(Page page) {
        if (cur == null) {
            cur = page;
            cache += cur.size;
            return;
        }
        front.clear();
        back.add(cur);
        cur = page;
        setCache();
        while (cache > C) {
            back.deleteLast();
            setCache();
        }
    }

    public static void compress() {
        if (back.isEmpty()) {
            return;
        }
        back.compress();
        setCache();
    }

    public static void setCache() {
        cache = back.size + front.size + cur.size;
    }
}

class Page {
    int number;
    int size;

    public Page(int number, int size) {
        this.number = number;
        this.size = size;
    }
}

class Store {
    Deque<Page> q;
    int size;

    Store() {
        q = new LinkedList<>();
        size = 0;
    }

    // 연속으로 같은 페이지 찾기 구현
    public void compress() {
        Iterator<Page> itr = q.iterator();
        Page prev = itr.next();
        while (itr.hasNext()) {
            Page cur = itr.next();
            if (prev.number == cur.number) {
                itr.remove();
                size -= cur.size;
            }
            prev = cur;
        }
    }

    public void deleteLast() {
        Page page = q.poll();
        size -= page.size;
    }

    public void clear() {
        q.clear();
        size = 0;
    }

    public boolean isEmpty() {
        return q.isEmpty();
    }

    public void add(Page page) {
        q.add(page);
        size += page.size;
    }

    public Page pop() {
        Page page = q.pollLast();
        size -= page.size;
        return page;
    }
}
