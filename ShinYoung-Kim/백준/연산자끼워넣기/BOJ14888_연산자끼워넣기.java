import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ14888_연산자끼워넣기 {
    static int n;
    static int[] numberArray;
    static int[] calArray;
    static int min = Integer.MAX_VALUE;
    static int max = Integer.MIN_VALUE;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        numberArray = new int[n];
        for (int i = 0; i < n; i++) {
            numberArray[i] = Integer.parseInt(stringTokenizer.nextToken());
        }

        calArray = new int[n - 1];
        stringTokenizer = new StringTokenizer(br.readLine());
        int index = 0;
        for (int i = 0; i < 4; i++) {
            int count = Integer.parseInt(stringTokenizer.nextToken());
            for (int j = 0; j < count; j++) {
                calArray[index] = i;
                index += 1;
            }
        }

        boolean[] visited = new boolean[n - 1];
        dfs(0, visited, numberArray[0]);
        System.out.println(max);
        System.out.println(min);
    }

    private static void dfs(int depth, boolean[] visited, int calculate) {
        if (depth == n - 1) {
            max = Math.max(max, calculate);
            min = Math.min(min, calculate);
            return;
        }

        for (int i = 0; i < n - 1; i++) {
            if (!visited[i]) {
                visited[i] = true;
                int temp = calculate(calArray[i], depth, calculate);
                dfs(depth + 1, visited, temp);
                visited[i] = false;
            }
        }
    }

    private static int calculate(int cal, int depth, int previous) {
        int temp = previous;
        switch (cal) {
            case 0:
                temp += numberArray[depth + 1];
                break;
            case 1:
                temp -= numberArray[depth + 1];
                break;
            case 2:
                temp *= numberArray[depth + 1];
                break;
            case 3:
                temp /= numberArray[depth + 1];
                break;
        }

        return temp;
    }
}
