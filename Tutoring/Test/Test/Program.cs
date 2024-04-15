using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    class Program
    {
        static void Main(string[] args)
        {

            int[] myNumbers = new int[3];
            int x = 0;
            int price = 0;
            int totalPrice = 0;

            while (x < 2)
            {

                try
                {
                    Console.Write("Please Enter a Price: ");
                    price = Convert.ToInt32(Console.ReadLine());
                    Console.WriteLine(price);
                    myNumbers[x] = price;
                    totalPrice += price;
                }
                catch (Exception e)
                {
                    Console.WriteLine("Your error is: " + e);
                }

                x++;

            }

            Console.WriteLine("Whats up Jabronies? Your array is ready bro: { " + myNumbers[0] + " " + myNumbers[1] + " }" );
            Console.WriteLine("Your grand total is: $" + totalPrice);
            Console.ReadLine();

        }
    }
}
