import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ1005_ACMCraft {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
            int buildingNumber = Integer.parseInt(stringTokenizer.nextToken());
            int conditionNumber = Integer.parseInt(stringTokenizer.nextToken());

            long[] timeArray = new long[buildingNumber + 1];
            long[] answerArray = new long[buildingNumber + 1];
            stringTokenizer = new StringTokenizer(br.readLine());
            for (int j = 1; j <= buildingNumber; j++) {
                timeArray[j] = Integer.parseInt(stringTokenizer.nextToken());
            }

            int[] array = new int[buildingNumber + 1];
            ArrayList<Integer>[] relation = new ArrayList[buildingNumber + 1];
            for (int j = 1; j <= buildingNumber; j++) {
                relation[j] = new ArrayList<>();
            }

            for (int j = 0; j < conditionNumber; j++) {
                stringTokenizer = new StringTokenizer(br.readLine());
                int before = Integer.parseInt(stringTokenizer.nextToken());
                int after = Integer.parseInt(stringTokenizer.nextToken());

                array[after] += 1;
                relation[before].add(after);
            }

            Queue<Integer> queue = new LinkedList<>();
            for (int j = 1; j <= buildingNumber; j++) {
                if (array[j] == 0) {
                    queue.add(j);
                }
                //answerArray[j] = timeArray[j];
            }


                while (!queue.isEmpty()) {
                    int index = queue.poll();
                    for (int next : relation[index]) {
                        array[next] -= 1;
                        if (array[next] == 0) {
                            queue.add(next);
                        }
                        //timeArray[next] += timeArray[index];
                        answerArray[next] = Math.max(answerArray[next], timeArray[index] + answerArray[index]);
                    }
                }


            int wanted = Integer.parseInt(br.readLine());
            sb.append(timeArray[wanted] + answerArray[wanted]).append("\n");
            //System.out.println(Arrays.toString(timeArray));
            //System.out.println(Arrays.toString(answerArray));
        }

        System.out.print(sb);
    }
}
