package input_output;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class A_10171 {
	public static void main(String[] args) throws IOException {
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		bw.write("\\    /\\ ");
		bw.write("\n )  ( ')");
		bw.write("\n(  /  )");
		bw.write("\n \\(__)|");
		bw.close();
	}

}
