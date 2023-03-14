import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class BOJ25240_가희와파일탐색기2 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        int userCount = Integer.parseInt(stringTokenizer.nextToken());
        int fileCount = Integer.parseInt(stringTokenizer.nextToken());

        //유저 이름 -> 그룹들
        HashMap<String, String[]> userGroupRelation = new HashMap<>();
        HashMap<String, String[]> fileInfoMap = new HashMap<>();
        //파일 이름 -> 123/주인/그룹

        for (int i = 0; i < userCount; i++) {
            String string = br.readLine();
            String[] groupArray = string.split(",| ");
            String user = groupArray[0] + "";

            userGroupRelation.put(user, groupArray);
        }

        for (int i = 0; i < fileCount; i++) {
            stringTokenizer = new StringTokenizer(br.readLine());
            String file = stringTokenizer.nextToken();
            String[] fileInfo = new String[3];

            for (int j = 0; j < 3; j++) {
                fileInfo[j] = stringTokenizer.nextToken();
            }

            fileInfoMap.put(file, fileInfo);
        }

        int count = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < count; i++) {
            stringTokenizer = new StringTokenizer(br.readLine());
            String user = stringTokenizer.nextToken();
            String file = stringTokenizer.nextToken();
            String operation = stringTokenizer.nextToken();
            int answer = -1;

            String[] fileInfo = fileInfoMap.get(file);
            if (fileInfo[1].equals(user)) {
                answer = isOperationPossible(fileInfo[0].charAt(0) - '0', operation);
            } else {
                String[] userGroup = userGroupRelation.get(user);
                boolean isGroup = false;
                for (int j = 0; j < userGroup.length; j++) {
                    if (userGroup[j] == null) {
                        break;
                    }

                    if (userGroup[j].equals(fileInfo[2])) {
                        answer = isOperationPossible(fileInfo[0].charAt(1) - '0', operation);
                        isGroup = true;
                        break;
                    }
                }

                if (!isGroup) {
                    answer = isOperationPossible(fileInfo[0].charAt(2) - '0', operation);
                }
            }

            if (i == count - 1) {
                sb.append(answer);
            } else {
                sb.append(answer).append("\n");
            }
        }

        //System.out.println(userGroupRelation);
        System.out.println(sb);
    }

    private static int isOperationPossible(int permission, String operation) {
        int temp = permission;
        boolean executable;
        boolean writable;
        boolean readable;

        if (temp / 4 > 0) {
            readable = true;
            temp -= 4;
        } else {
            readable = false;
        }

        if (temp / 2 > 0) {
            writable = true;
            readable = true;
            temp -= 2;
        } else {
            writable = false;
        }

        if (temp > 0) {
            executable = true;
        } else {
            executable = false;
        }

        if (operation.equals("R")) {
            if (readable) {
                return 1;
            } else {
                return 0;
            }
        } else if (operation.equals("W")) {
            if (writable) {
                return 1;
            } else {
                return 0;
            }
        } else {
            if (executable) {
                return 1;
            } else {
                return 0;
            }
        }
    }
}
