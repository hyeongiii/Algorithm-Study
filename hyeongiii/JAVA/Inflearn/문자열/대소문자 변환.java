import java.io.*;
import java.util.*;

public class Main {

    private static String answer = "";
    private static String word;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        word = br.readLine();

        for(int i = 0; i < word.length(); i++) {
            if (Character.isUpperCase(word.charAt(i))) {
                answer += Character.toLowerCase(word.charAt(i));
            }
            else {
                answer += Character.toUpperCase(word.charAt(i));
            }
        }

        System.out.println(answer);
    }

    // 강사님 풀이
    public String solution(String str) {
        String answer = "";

        for (char c : str.toCharArray()) {
            if (x >= 97 && x <= 122) {
                answer += (char)(x - 32);
            }
            else {
                answer += (char)(x + 32);
            }
        }
    }
}