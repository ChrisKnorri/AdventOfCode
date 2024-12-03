using System;
using System.IO;

class Day_01
{
    static void Main()
    {
        string[] lines = File.ReadAllLines("/home/knorri/projects/AOC24/day_01/list.txt");
        
        // Output the lines to verify
        foreach (string line in lines)
        {
            Console.WriteLine(line);
        }
    }
}