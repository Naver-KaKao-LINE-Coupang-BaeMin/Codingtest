import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ3030_테니스 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] player = br.readLine().split(" ");
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
            int leftWin = 0;
            int rightWin = 0;
            boolean isFinished = false;
            int index = 0;
            boolean isFalse = false;

            while (stringTokenizer.hasMoreTokens()) {
                index += 1;
                if (isFinished) {
                    isFalse = true;
                    break;
                }
                String[] score = stringTokenizer.nextToken().split(":");
                int leftScore = Integer.parseInt(score[0]);
                int rightScore = Integer.parseInt(score[1]);

                if (leftScore > rightScore) {
                    leftWin += 1;
                    if (leftWin == 2) {
                        isFinished = true;
                    }

                    if (!isWin(leftScore, rightScore, index)) {
                        isFalse = true;
                    }

                    if (player[1].equals("federer")) {
                        isFalse = true;
                    }
                } else if (leftScore < rightScore) {
                    rightWin += 1;
                    if (rightWin == 2) {
                        isFinished = true;
                    }

                    if (!isWin(rightScore, leftScore, index)) {
                        isFalse = true;
                    }

                    if (player[0].equals("federer")) {
                        isFalse = true;
                    }
                } else if (leftScore == rightScore) {
                    isFalse = true;
                }
            }

            if (!isFinished || leftWin == rightWin) {
                isFalse = true;
            }

            if (isFalse) {
                sb.append("ne").append("\n");
            } else {
                sb.append("da").append("\n");
            }
        }

        System.out.println(sb);
    }

    private static boolean isWin(int leftScore, int rightScore, int index) {
        int diff = leftScore - rightScore;

        if (leftScore >= 6 && rightScore >= 6) {
            if ((index == 1 || index == 2)) {
                if (diff == 1) {
                    return true;
                }
            } else {
                if (diff == 2) {
                    return true;
                }
            }
        } else if (leftScore >= 6 && rightScore < 6) {
            if (diff >= 2) {
                return true;
            }
        }

        return false;
    }
}
