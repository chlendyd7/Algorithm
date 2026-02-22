import java.io.*;
import java.util.*;
/*
 * (학점x과목평균) 의 합을 학점의 총합으로 나눈 값
 *  전공평점 3.3이상
 * 학점x
 * 등급이 p는 계산에서 제외
 * 
 * 과목명, 학점, 등급
 * 
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        double totalScore = 0.0;
        double sumScore = 0.0;
        Map<String, Double> gradeMap = new HashMap<>();
        gradeMap.put("A+", 4.5);
        gradeMap.put("A0", 4.0);
        gradeMap.put("B+", 3.5);
        gradeMap.put("B0", 3.0);
        gradeMap.put("C+", 2.5);
        gradeMap.put("C0", 2.0);
        gradeMap.put("D+", 1.5);
        gradeMap.put("D0", 1.0);
        gradeMap.put("F", 0.0);

        for (int i=0; i< 20; i++) {
            String[] input = br.readLine().split(" ");
            String subject = input[0];
            double score = Double.parseDouble(input[1]);
            String grade = input[2];

            if (grade.equals("P")) continue;

            sumScore += score * gradeMap.get(grade);
            totalScore += score;
        }
        System.out.printf("%.64\n", sumScore / totalScore);
    }
}