import java.io.*;
import java.util.*;

public class Main {
    static FastReader scan = new FastReader();
    static String doc, word;
    static int startIdx, findIdx, count = 0;

    static int idx, answer = 0;

    static void input() {
        doc = scan.nextLine();
        word = scan.nextLine();
    }

    // 강의 풀이
    static int countWordFastCamp(String doc, String word) {
        while (true) {
            findIdx = doc.indexOf(word, startIdx);
            // 반복문 종료 조건
            if (findIdx < 0) {
                break;
            }
            count++;
            startIdx = findIdx + word.length();
        }
        return count;
    }

    // 내가 푼 방식 (겁나 복잡하게 풀었다고 한다,,,,)
    static int countWordHyeongiii(String doc, String word, int idx) {
        // str의 현재 위치에서 word 단어가 나올 수 없는 경우 반복문 종료
        if (idx + word.length() - 1 >= doc.length()) {
            return answer;
        }

        // word 인덱스와 str의 인덱스를 비교
        for (int j = 0; j < word.length(); j++) {
            if (word.charAt(j) == doc.charAt(idx + j)) {
                if (j == word.length() - 1) {
                    answer += 1;
                    idx += word.length();
                }
            } else {
                idx += 1;
                break;
            }
        }
        return countWord(doc, word, idx);
    }

    public static void main(String[] args) {
        input();
        System.out.println(countWordFastCamp(doc, word));
        System.out.println(countWordHyeongiii(doc, word, idx));
    }

    public static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}