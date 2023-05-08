/**
 * 한 개의 문자열을 입력받고, 특정 문자를 입력받아 해당 특정 문자가 입력받은 문자열에 몇 개 존재하는지 알아내는 프로그램을 작성하라.
 * 대소문자를 구분하지 않고, 문자열의 길이는 100을 넘지 않는다.
 *
 * 입력 : 첫 줄에 문자열이 주어지고, 두 번째 줄에 문자가 주어진다.
 *       문자열은 영어 알파벳으로만 구성되어 있다.
 * 출력 : 첫 줄에 해당 문자의 개수를 출력한다.
 *
 * 입력 예시 : Computercooler
 *           c
 * 출력 예시 : 2
 */

import java.util.*;
import java.io.*;

public class Main {

    private static String word;
    private static String ch;
    private static int answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        word = br.readLine();
        ch = br.readLine();

        word = word.toLowerCase();
        ch = ch.toLowerCase();

        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == ch.charAt(0)) {
                answer += 1;
            }
        }

        /*
        향상된 for 문으로도 사용 가능

        for (char x : str.toCharArray()) {
            if (x == ch) {
                answer ++;
            }
        }
         */

        System.out.println(answer);
    }

}