import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       String[] input = br.readLine().split(" ");
       String a = input[0];
       String b = input[1];

       int minDiff = 50;
       for (int i=0; i<=b.length() - a.length(); i++) {
        int currentDiff = 0;
        for (int j=0; j<a.length(); j++) {
            if (a.charAt(j) != b.charAt(i+j)){
                currentDiff ++;
            }
        }
        if (currentDiff < minDiff) {
            minDiff = currentDiff;
        }
       }
       System.out.println(minDiff);
        
    }
}
