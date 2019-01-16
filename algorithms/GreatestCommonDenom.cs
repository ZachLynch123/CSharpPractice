using System;

namespace algorithms
{
    class GreatestCommonDenom
    {
        public int common (int a, int b) {
            while (b != 0) {
                int temp = a;
                a = b;
                b = temp % b;
            }
            return a;
        }
        static void Main(string[] args)
        {
            var p = new GreatestCommonDenom();
            int result = p.common(20, 8);
            Console.WriteLine(result);
        }
    }
}
