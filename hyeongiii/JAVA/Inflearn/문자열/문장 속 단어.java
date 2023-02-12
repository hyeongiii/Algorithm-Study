/**
 * 한 개의 문장이 주어지면 그 문장 속에서 가장 긴 단어를 출력하는 프로그램을 작성해라
 * 문장속의 각 단어는 공백으로 구분된다.
 *
 * 입력: 첫 줄에 길이가 100을 넘지 않는 한 개의 문장이 주어진다. 문장은 영어 알파벳으로만 구성되어 있다.
 * 출력: 첫 줄에 가장 긴 단어를 출력한다. 가장 길이가 긴 단어가 여러개일 경우 문장속에서 가장 앞쪽에 위치한 단어를 답으로 한다.
 *
 * 예시 입력: it is time to study
 * 예시 출력: study
 */

import java.util.*;
import java.io.*;

public class Main {

    private static String data;
    private static String answer;
    private static int num = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        while (st.hasMoreTokens()) {
            data = st.nextToken();

            if (num < data.length()) {
                num = data.length();
                answer = data;
            }
        }

        System.out.println(answer);

    }

    // 강사님 풀이 1
    public String solution1(String str) {
        String answer = "";

        int m = Integer.MIN_VALUE;    // 가장 작은 값으로 초기화
        String[] s = str.split(' ');

        for (String x : s) {
            int len = x.length();
            if(len > m) {
                m = len;
                answer = x
            }
        }

        return answer;
    }

    // 강사님 풀이 2
    public String solution2(String str) {
        String answer = "";

        int m = Integer.MIN_VALUE;
        int pos;

        while ((pos = str.indexOf(' ')) != -1) {
            String tmp = str.substring(0, pos);
            int len = tmp.length();

            if (len > m) {
                m = len;
                answer = tmp;
            }

            str = str.substring(pos + 1);
        }

        // 가장 마지막 단어
        if (str.length() > m) {
            answer = str;
        }


        return answer;
    }
}