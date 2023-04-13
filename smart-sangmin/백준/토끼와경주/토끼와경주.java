import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int Q = Integer.parseInt(br.readLine());
        // 100
        StringTokenizer st = new StringTokenizer(br.readLine());
        st.nextToken();

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        HashMap<Integer, Rabbit> rs = new HashMap<>();
        for (int i = 0; i < P; i++) {
            int pid = Integer.parseInt(st.nextToken());
            long distance = Integer.parseInt(st.nextToken());
            rs.put(pid, new Rabbit(pid, distance));
        }
        PriorityQueue<Rabbit> queue = new PriorityQueue<>(); // 대기열
        queue.addAll(rs.values());
        for (int i = 1; i < Q - 1; i++) {
            st = new StringTokenizer(br.readLine());
            switch (st.nextToken()) {
                case "200":  // 경주 진행 K = round, S는 round가 모두 지난 후 한번이라도 뽑힌 토끼중에 가장 우선 순위가 높은 애 골라줌
                    int K = Integer.parseInt(st.nextToken());
                    int S = Integer.parseInt(st.nextToken());
                    HashMap<Integer, Boolean> isRan = new HashMap<>();
                    while (K-- > 0) {
                        Rabbit r = queue.poll();
                        long addScore = r.jump(N, M);
                        scoreUp(rs, r.pid, addScore);
                        queue.add(r);
                        isRan.put(r.pid, true);
                    }
                    lastAction(rs, isRan, S);
                    break;
                case "300": // 이동거리 변경, 200 하기 전에 실행 될 수 있음?
                    int pid = Integer.parseInt(st.nextToken());
                    long L = Long.parseLong(st.nextToken());
                    Rabbit rabbit = rs.get(pid);
                    rabbit.setDistance(L);
                    // System.out.println("Rabbit: " + rabbit.pid + " len: " + rabbit.distance);
                    break;
            }
        }
        br.readLine(); // 400
        System.out.print(bestScore(rs));
    }

    public static void lastAction(HashMap<Integer, Rabbit> rs, HashMap<Integer, Boolean> isRan, int score) {
        if (isRan.size() == 0){
            return;
        }
        ArrayList<Rabbit> temp = new ArrayList<>(rs.values());
        temp.sort(new Comparator<Rabbit>() {
            @Override
            public int compare(Rabbit o1, Rabbit o2) {
                if (o2.row + o2.col < o1.row + o1.col) { // 행+열이 낮은 애가 우선순위 높음
                    return -1;
                } else if (o2.row + o2.col > o1.row + o1.col) {
                    return 1;
                } else {
                    if (o2.row < o1.row) {
                        return -1;
                    } else if (o2.row > o1.row) {
                        return 1;
                    } else {
                        if (o2.col < o1.col) {
                            return -1;
                        } else if (o2.col > o1.col) {
                            return 1;
                        } else {
                            if (o2.pid < o1.pid) {
                                return -1;
                            } else if (o2.pid > o1.pid) {
                                return 1;
                            } else {
                                return 0;
                            }
                        }
                    }
                }
            }
        });

        for (Rabbit rabbit : temp) {
            if (isRan.getOrDefault(rabbit.pid, false)){
                rabbit.score += score;
                break;
            }
        }
    }

    public static long bestScore(HashMap<Integer, Rabbit> rs) {
        long best = -1;
        for (Map.Entry<Integer, Rabbit> entry : rs.entrySet()) {
            best = Math.max(best, entry.getValue().score);
//            System.out.println("pid: " + entry.getValue().pid +" score: " + entry.getValue().score + " row: (" +entry.getValue().row + ", " + entry.getValue().col+")");
        }
        return best;
    }

    public static void scoreUp(HashMap<Integer, Rabbit> rs, int pid, long score) {
        for (Integer key : rs.keySet()) {
            if (key == pid) {
                continue;
            }
            rs.get(key).score += score;
        }
    }
}

class Rabbit implements Comparable<Rabbit> {
    int pid;
    long distance;
    long score;
    int row;
    int col;
    int jumpCnt;

    Rabbit(int pid, long distance) {
        this.pid = pid;
        this.distance = distance;
        this.score = 0;
        this.jumpCnt = 0;
        this.row = 0;
        this.col = 0;
    }


    public long jump(int N, int M) {
        Coordinate ret = new Coordinate(0, 0);
        int[][] direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        // System.out.println("****pid: " + pid + " row: " + row + " col: " + col);
        for (int[] d : direction) {
            long y = (this.row + (d[0] * this.distance)) % ((N - 1) * 2L);
            long x = (this.col + (d[1] * this.distance)) % ((M - 1) * 2L);
            // row 넘었을 때, 왔다 갔다 하면서 두 번 이상 꺾일 수도 있음
            int moveY = d[0];
            int moveX = d[1];
            while (y < 0 || y >= N) { // 안에 들어올 때 까지 반복
                if (y < 0) {
                    moveY *= -1;
                    long over = -y;
                    y = over * moveY;
                } else if (y >= N) {
                    moveY *= -1;
                    long over = y - N + 1;
                    y = N - 1 + (over * moveY);
                }
                // System.out.println("y: " + y);
            }
            // col이 넘었을 때, 왔다 갔다 하면서 두 번 이상 꺾일 수 도 있음
            while (x < 0 || x >= M) { // 안에 들어올 때 까지 반복
                if (x < 0) {
                    moveX *= -1;
                    long over = -x;
                    x = over * moveX;
                } else if (x >= M) {
                    moveX *= -1;
                    long over = x - M + 1;
                    x = M - 1 + (over * moveX);
                }
                // System.out.println("x: " + x);
            }
            Coordinate c = new Coordinate((int) y, (int) x);
            if (ret.compareTo(c) == 1) {
                ret = c;
            }
        }
        this.row = ret.row;
        this.col = ret.col;
        this.jumpCnt++;
        long r = ret.row;
        long c = ret.col;
        return r + c + 2;
    }

    public void setDistance(long L) {
        this.distance *= L;
    }

    public int compareTo(Rabbit o) {
        // 1번째 총 점프 횟수
        if (this.jumpCnt < o.jumpCnt) { // 내가 더 점프 횟수가 낮으니까 우선순위 높음
            return -1;
        } else if (this.jumpCnt > o.jumpCnt) { // 내가 더 점수 횟수 높으니까 우선순위 낮음
            return 1;
        } else { // 점프 횟수 같을 때 2번째, 행번호 + 열번호
            if (this.row + this.col < o.row + o.col) { // 행+열이 낮은 애가 우선순위 높음
                return -1;
            } else if (this.row + this.col > o.row + o.col) {
                return 1;
            } else {
                if (this.row < o.row) {
                    return -1;
                } else if (this.row > o.row) {
                    return 1;
                } else {
                    if (this.col < o.col) {
                        return -1;
                    } else if (this.col > o.col) {
                        return 1;
                    } else {
                        return Integer.compare(this.pid, o.pid);
                    }
                }
            }
        }
    }
}

class Coordinate implements Comparable<Coordinate> {
    int row;
    int col;

    public Coordinate(int row, int col) {
        this.row = row;
        this.col = col;
    }

    public int compareTo(Coordinate o) {
        if (this.row + this.col > o.row + o.col) { // -1이 우선순위 클 떄고 1이 우선순위 낮을 떄
            return -1;
        } else if (this.row + this.col < o.row + o.col) {
            return 1;
        } else {
            if (this.row > o.row) { // -1이 우선순위 클 떄고 1이 우선순위 낮을 떄
                return -1;
            } else if (this.row < o.row) {
                return 1;
            } else {
                if (this.col > o.col) { // -1이 우선순위 클 떄고 1이 우선순위 낮을 떄
                    return -1;
                } else if (this.col < o.col) {
                    return 1;
                } else {
                    return 0;
                }
            }
        }
    }
}