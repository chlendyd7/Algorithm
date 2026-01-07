public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        
        Integer n = Integer.parseInt(input[0]);
        Integer jimin = Integer.parseInt(input[1]);
        Integer hansu = Integer.parseInt(input[2]);
        
        Integer count = 0;
        while (!jimin == hansu) {
            jimin = (jimin + 1) / 2
            hansu = (hansu + 1) / 2

            count ++;
        }
        System.out.println(count);
    }
}
