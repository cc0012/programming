using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            // Deklaration von Variablen
            double Radius;
            double Umfang;
            double Oberflaeche;
            double Volumen;
            string eingabe;

            // Eingabe von Radius
            Console.Write("Radius (in cm): ");
            eingabe = Console.ReadLine();
            Radius = Convert.ToInt32(eingabe);

            //Berechnungen
            Umfang = Math.PI * 2 * Radius;
            Oberflaeche = 4 * Math.PI * Radius * Radius;
            Volumen = 4 / 3 * Math.PI * Radius * Radius * Radius;

            //Ausgabe
            Console.WriteLine("Umfang / Oberflaeche / Volumen = " + Umfang + " cm / " + Oberflaeche + " cm² / " + Volumen + " cm³ / ");

            Console.Read();
        }
    }
}
