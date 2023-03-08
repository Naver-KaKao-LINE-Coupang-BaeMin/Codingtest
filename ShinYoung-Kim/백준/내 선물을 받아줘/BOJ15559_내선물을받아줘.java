import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class BOJ15559_내선물을받아줘_re {
    static int x = 0;
    static int y = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());
        char[][] map = new char[n][m];
        boolean[][] visited = new boolean[n][m];
        boolean[][] isCycle = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String string = br.readLine();
            for (int j = 0; j < m; j++) {
                map[i][j] = string.charAt(j);
            }
        }

        int answer = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j]) {
                    answer += 1;
                    x = i;
                    y = j;
                    Queue<int[]> queue = new LinkedList<>();

                    while (!visited[x][y]) {
                        visited[x][y] = true;
                        queue.add(new int[]{x, y});

                        switch (map[x][y]) {
                            case 'N':
                                x -= 1;
                                break;
                            case 'S':
                                x += 1;
                                break;
                            case 'W':
                                y -= 1;
                                break;
                            case 'E':
                                y += 1;
                                break;
                        }

                        queue.add(new int[]{x, y});

                        if (isCycle[x][y]) {
                            answer -= 1;
                        }
                    }

                    while(!queue.isEmpty()) {
                        int[] temp = queue.poll();
                        isCycle[temp[0]][temp[1]] = true;
                    }
                }
            }
        }

        bw.write("" + answer);
        bw.flush();
        bw.close();
    }
}

