import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T;
        String st;
        T = Integer.parseInt(br.readLine());
        for (int i=0; i<T; i++) {
            st = br.readLine();
            System.out.println(""+ st.charAt(0)+st.charAt(st.length()-1));
        }
        
    }    
}
