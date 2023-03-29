import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//1. 세트를 승리하려면, 6게임 또는 그 이상을 이겼고, 적어도 상대편보다 두 게임 이상을 이겨야 한다.
// 세트: 6(게임):2(게임)
//2. 만약 "첫 번째 또는 두 번째 세트"의 결과가 6:6이라면, 세트의 승자를 가리기 위한 게임 한 판을 진행한다.
//
//3. 2 세트를 먼저 이긴 사람이 테니스 경기의 승자이다.

//sampras agassi
//6
//6:2 6:4
//3:6 7:5 2:6
//6:5 7:4
//7:6 7:6
//6:2 3:6
//6:2 1:6 6:8

public class 테니스 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String PlayerA = st.nextToken();
        String PlayerB = st.nextToken();
        // 페더러
        boolean A = PlayerA.equals("federer");
        boolean B = PlayerB.equals("federer");

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int sa = 1;
            int winA = 0;
            int winB = 0;
            String res = "";
            while (st.hasMoreTokens()) {
                if (winA == 2 || winB == 2) {
                    res = "ne";
                    break;
                }
                StringTokenizer s = new StringTokenizer(st.nextToken(), ":");
                int scA = Integer.parseInt(s.nextToken());
                int scB = Integer.parseInt(s.nextToken());
                int r = 0;
                if (sa == 1 || sa == 2) {
                    r = please(scA, scB, true);
                } else {
                    r = please(scA, scB, false);
                }
                if (r == 0) {
                    if (B) {
                        res = "ne";
                        break;
                    }
                    winA++;
                } else if (r == 1) {
                    if (A) {
                        res = "ne";
                        break;
                    }
                    winB++;
                } else {
                    res = "ne";
                    break;
                }
                sa++;
            }
            if (res.length() == 0) {
                if (winA == 2 || winB == 2) {
                    res = "da";
                } else {
                    res = "ne";
                }
            }
            System.out.println(res);
        }
    }

    public static int please(int scoreA, int scoreB, boolean isOneOrTwo) {
        int res;
        if (Math.abs(scoreA - scoreB) == 1 && isOneOrTwo) {
            if (scoreA == 7 && scoreB == 6) {
                res = 0;
            } else if (scoreA == 6 && scoreB == 7) {
                res = 1;
            } else {
                res = -1;
            }
        } else if (Math.abs(scoreA - scoreB) == 2) {
            if (isOneOrTwo) {
                if (scoreA == 6 && scoreB == 4 || scoreA == 7 && scoreB == 5) {
                    res = 0;
                } else if (scoreA == 4 && scoreB == 6 || scoreA == 5 && scoreB == 7) {
                    res = 1;
                } else {
                    res = -1;
                }
            } else {
                if (scoreA >= 6 && scoreA > scoreB) {
                    res = 0;
                } else if (scoreB >= 6 && scoreB > scoreA) {
                    res = 1;
                } else {
                    res = -1;
                }
            }
        } else if (Math.abs(scoreA - scoreB) > 2) {
            if (scoreA == 6 && scoreB < 4) {
                res = 0;
            } else if (scoreB == 6 && scoreA < 4) {
                res = 1;
            } else {
                res = -1;
            }
        } else {
            res = -1;
        }
        return res;
    }
}

