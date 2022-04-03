using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace A_10950
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] num = new int[int.Parse(Console.ReadLine())];
            int[] sum = new int[num.Length];

            for(int i =0; i<num.Length; i++)
            {
                string[] plus = Console.ReadLine().Split();
                sum[i] = int.Parse(plus[0]) + int.Parse(plus[1]);
            }
            for(int i=0; i<num.Length; i++)
                Console.WriteLine(sum[i]);

            Console.Read();
        }
    }
}
