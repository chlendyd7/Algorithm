package input_output;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class A_10172 {

	public static void main(String[] args) throws IOException {
		
			BufferedWriter bf = new BufferedWriter(new OutputStreamWriter(System.out));
	
			bf.write("|\\_/|");
			bf.write("\n|q p|   /}");
			bf.write("\n( 0 )\"\"\"\\");
			bf.write("\n|\"^\"`    |");
			bf.write("\n||_/=\\\\__|");
			bf.close();
	}

}
