import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String inputs = br.readLine();
        boolean check = false;
        for (int i=0; i<inputs.length()/2; i++) {
            if (inputs.charAt(i) != inputs.charAt(inputs.length() - i - 1)) {
                System.out.print(0);
                check = true;
                break;
            }
        }
        if (!check) System.out.println(1);
    }
}
