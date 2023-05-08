import java.util.*;
import java.io.*;

public class Main {

    static String data;
    static char answer;
    static int num = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        data = br.readLine().toUpperCase();
        // 알파벳 개수를 저장할 배열 선언 (알파벳 개수: 26)
        int[] arr = new int[26];

        for (int i = 0; i < data.length(); i++) {
            arr[(int)data.charAt(i) - 65] += 1;
        }

        for (int i = 0; i < 26; i++) {
            if (num < arr[i]) {
                answer = (char)(i + 65);
                num = arr[i];
            }
            else if (num == arr[i]) {
                answer = '?';
            }
        }

        System.out.println(answer);

    }
}