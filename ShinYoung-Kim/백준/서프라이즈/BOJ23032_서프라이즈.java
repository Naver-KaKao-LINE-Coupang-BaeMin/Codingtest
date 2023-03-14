import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BOJ23032_서프라이즈 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] array = new int[n];
        int sum = 0;
        int min = Integer.MAX_VALUE;

        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            array[i] = Integer.parseInt(stringTokenizer.nextToken());
        }

        for (int mid = 1; mid < n; mid++) {
            int leftSum = array[mid - 1];
            int rightSum = array[mid];
            int left = mid - 1;
            int right = mid;
            int diff = Math.abs(leftSum - rightSum);
            int currentSum = rightSum + leftSum;

            if (diff < min) {
                min = diff;
                sum = currentSum;
            } else if (diff == min) {
                if (sum < rightSum) {
                    sum = currentSum;
                }
            }
            while (left <= right) {
                if (leftSum < rightSum) {
                    left -= 1;
                    if (left < 0) {
                        break;
                    }

                    leftSum += array[left];

                    diff = Math.abs(leftSum - rightSum);
                    currentSum = rightSum + leftSum;
                    if (diff < min) {
                        min = diff;
                        sum = currentSum;
                    } else if (diff == min) {
                        if (sum < currentSum) {
                            sum = currentSum;
                        }
                    }
                } else if (leftSum > rightSum) {
                    right += 1;
                    if (right >= n) {
                        break;
                    }

                    rightSum += array[right];

                    diff = Math.abs(leftSum - rightSum);
                    currentSum = rightSum + leftSum;
                    if (diff < min) {
                        min = diff;
                        sum = currentSum;
                    } else if (diff == min) {
                        if (sum < currentSum) {
                            sum = currentSum;
                        }
                    }
                } else {
                    left -= 1;
                    right += 1;
                    if (left < 0) {
                        break;
                    }

                    if (right >= n) {
                        break;
                    }
                    leftSum += array[left];
                    rightSum += array[right];

                    diff = Math.abs(leftSum - rightSum);
                    currentSum = rightSum + leftSum;
                    if (diff < min) {
                        min = diff;
                        sum = currentSum;
                    } else if (diff == min) {
                        if (sum < currentSum) {
                            sum = currentSum;
                        }
                    }
                }
            }
        }

        System.out.println(sum);
    }
}
