import java.util.*;
import java.io.*;

public class 포탑부수기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        Tower[][] maps = new Tower[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                maps[i][j] = new Tower(Integer.parseInt(st.nextToken()), i, j);
            }
        }
        int answer = 0;
        while (K-- > 0) {
            Tower attacker = new Tower(5001, 1, 1);
            Tower defenser = new Tower(-1, N, M);
            for (int i = 0; i < N; i++) {  // attack defense 찾기
                for (int j = 0; j < M; j++) {
                    if (attacker.compareTo(maps[i][j]) == 1 && maps[i][j].getPower() != 0) {
                        attacker = maps[i][j];
                    }
                    if (defenser.compareTo(maps[i][j]) == -1 && maps[i][j].getPower() != 0) {
                        defenser = maps[i][j];
                    }
                }
            }
            if (attacker == defenser) { // 한개밖에 없거나
                answer -= 1;
                break;
            } else if (attacker.getPower() == 5001 && defenser.getPower() == -1) { // 올 0이거나
                answer = 0;
                break;
            }


            attacker.imAttacker(N, M);
            String shortestPath = attacker.getShortestPath(maps, defenser);
            ArrayList<int[]> destroyed;
            // shortestPath = "can't reach";
            if (shortestPath.equals("can't reach")) {
                destroyed = attacker.bomb(maps, defenser);
            } else {
                destroyed = attacker.razer(maps, shortestPath);
            }
            answer = heal(maps, destroyed, N, M);
//            for (int i = 0; i < N; i++) {
//                for (int j = 0; j < M; j++) {
//                    System.out.print(maps[i][j].power + " ");
//                }
//                System.out.println();
//            }
//            System.out.println();
        }

        // for (int i = 0; i < N; i++) {
        //     for (int j = 0; j < M; j++) {
        //         System.out.print(maps[i][j].power + " ");
        //     }
        //     System.out.println();
        // }

        System.out.print(answer);
    }

    public static int heal(Tower[][] maps, ArrayList<int[]> destroyed, int N, int M) {
        int ret = -1;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int[] some = {i, j};
                if (maps[i][j].power != 0 && !check(destroyed, some))
                    maps[i][j].power += 1;
                ret = Math.max(maps[i][j].power, ret);
            }
        }
        return ret;
    }

    public static boolean check(ArrayList<int[]> list, int[] some) {
        for (int[] element : list) {
            if (Arrays.equals(element, some)) {
                return true;
            }
        }
        return false;
    }
}

class Tower implements Comparable<Tower> {
    int power;
    int attack;
    int row, col;

    Tower(int power, int row, int col) {
        this.power = power;
        this.row = row;
        this.col = col;
        this.attack = 0;
    }

    public int compareTo(Tower o) {
        if (this.power > o.power) {
            return 1;
        } else if (this.power < o.power) {  // 공격력이 가장 낮을 떄
            return -1;
        } else {
            if (this.attack < o.attack) {
                return 1;
            } else if (this.attack > o.attack) {  // 가장 최근 공격했을 때
                return -1;
            } else {
                if (this.row + this.col < o.row + o.col) {
                    return 1;
                } else if (this.row + this.col > o.row + o.col) {  // 행과 열이 클 때
                    return -1;
                } else {
                    if (this.col < o.col) {
                        return 1;
                    } else if (this.col > o.col) {  // 열값이 클 때
                        return -1;
                    }
                }
            }
        }
        return 0;
    }

    public int getPower() {
        return this.power;
    }

    public int getAttack() {
        return this.attack;
    }

    public int getRow() {
        return this.row;
    }

    public int getCol() {
        return this.col;
    }

    public String toString() {
        return this.getPower() + " " + this.getAttack() + " " + this.getRow() + " " + this.getCol();
    }

    public void imAttacker(int N, int M) {
        this.power += (N + M);
    }

    public String getShortestPath(Tower[][] maps, Tower target) {
        this.attack++;
        int[][] direction = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int N = maps.length;
        int M = maps[0].length;
        boolean[][] visited = new boolean[N][M];

        StringTokenizer st;
        Queue<String> queue = new LinkedList<>();
        String temp = this.getRow() + "" + this.getCol();
        queue.add(temp);
        while (!queue.isEmpty()) {
            String path = queue.poll();
            st = new StringTokenizer(path);

            String coor = st.nextToken();
            int y = coor.charAt(0) - '0';
            int x = coor.charAt(1) - '0';
            if (y == target.getRow() && x == target.getCol()) {
                return path;
            }
            for (int i = 0; i < 4; i++) {
                int[] d = direction[i];
                int goY = (d[0] + y + N) % N;
                int goX = (d[1] + x + M) % M;
                if (!visited[goY][goX] && maps[goY][goX].power != 0) {
                    String newPath = goY + "" + goX + " " + path;
                    queue.add(newPath);
                    visited[goY][goX] = true;
                }
            }
        }

        return "can't reach";
    }

    public ArrayList<int[]> razer(Tower[][] maps, String path) {
        ArrayList<int[]> destroyed = new ArrayList<>();
        destroyed.add(new int[]{this.row, this.col});
        StringTokenizer st = new StringTokenizer(path);
        String end = st.nextToken(); // target Tower
        int y = end.charAt(0) - '0';
        int x = end.charAt(1) - '0';
        Tower target = maps[y][x];
        destroyed.add(new int[]{y, x});
        target.power = target.power - this.power;
        if (target.power < 0) {
            target.power = 0;
        }

        while (st.countTokens() > 1) {  // between target and attacker
            String coor = st.nextToken();
            y = coor.charAt(0) - '0';
            x = coor.charAt(1) - '0';
            Tower between = maps[y][x];
            destroyed.add(new int[]{y, x});
            between.power = between.power - (this.power / 2);
            if (between.power < 0) {
                between.power = 0;
            }
        }
        return destroyed;
    }

    public ArrayList<int[]> bomb(Tower[][] maps, Tower target) {
        ArrayList<int[]> destroyed = new ArrayList<>();
        destroyed.add(new int[]{this.row, this.col});
        int N = maps.length;
        int M = maps[0].length;
        int[][] direction = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
        if (this.power == 289){
            System.out.println();
        }
        int y = target.getRow();
        int x = target.getCol();

        destroyed.add(new int[]{y, x});
        target.power -= this.power;
        if (maps[y][x].power < 0) {
            maps[y][x].power = 0;
        }

        for (int i = 0; i < 8; i++) {
            int[] d = direction[i];
            int goY = d[0] + y;
            if (goY < 0) {
                goY = N - 1;
            } else if (goY > N - 1) {
                goY = 0;
            }
            int goX = d[1] + x;
            if (goX < 0) {
                goX = M - 1;
            } else if (goX > M - 1) {
                goX = 0;
            }
            if (goY == this.row && goX == this.col) {
                continue;
            }
            if (maps[goY][goX].power != 0) {
                maps[goY][goX].power = maps[goY][goX].power - (this.power / 2);
                if (maps[goY][goX].power < 0) {
                    maps[goY][goX].power = 0;
                }
                destroyed.add(new int[]{goY, goX});
            }
        }

        return destroyed;
    }
}