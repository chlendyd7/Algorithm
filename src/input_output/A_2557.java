package input_output;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class A_2557 {
	public static void main(String[] args) throws IOException {
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		bw.write("Hello World!");
		bw.close();
	}

}
