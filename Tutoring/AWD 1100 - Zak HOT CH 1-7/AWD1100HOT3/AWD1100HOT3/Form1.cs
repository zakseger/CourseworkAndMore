using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AWD1100HOT3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            // Add a Button Click Event handler 
            calculateBtn.Click += new EventHandler(calculateBtn_Click);
            clearBtn.Click += new EventHandler(clearBtn_Click);

        }

        public const string INFOTECHNOLOGY = "INFO TECHNOLOGY";
        public const string WEBDEVELOPMENT = "WEB DEVELOPMENT";
        public const string PROGRAMMING = "PRGRAMMING";
        public const string ACCOUNTING = "ACCOUNTING";
        public const string SHIPPING = "SHIPPING";

        public const double minHrsWorked = 0;
        public const double maxHrsWorked = 84;
        public const double minHrlyRate = 0;
        public const double maxHrlyRate = 99.99;
        public const double maxHrsNoOT = 40;
        public const double overtimeRate = 1.5;

        private void calculateBtn_Click(object sender, EventArgs e)
        {

            try
            {
                if (firstNameTxt.Text == "")
                {
                    throw new Exception("You must enter a first name.");
                }
                string firstName = firstNameTxt.Text;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Exception caught: " + ex.Message);
            }

            try
            {
                if (lastNameTxt.Text == "")
                {
                    throw new Exception("You must enter a last name.");
                }
                string lastName = lastNameTxt.Text;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Exception caught: " + ex.Message);
            }

            try
            {
                if (departmentTxt.Text == "")
                {
                    throw new Exception("You must enter a department.");
                }
                if (departmentTxt.Text != WEBDEVELOPMENT && departmentTxt.Text != INFOTECHNOLOGY && departmentTxt.Text != ACCOUNTING && departmentTxt.Text != PROGRAMMING && departmentTxt.Text != SHIPPING )
                {
                    throw new Exception("You must enter a CORRECT department.");
                }
                string department = firstNameTxt.Text;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Exception caught: " + ex.Message);
            }

            try
            {
                if (hoursWorkedTxt.Text == "")
                {
                    throw new Exception("You must enter an hours worked amount.");
                }
                double hoursWorked = Double.Parse(hoursWorkedTxt.Text);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Exception caught: " + ex.Message);
            }

            try
            {
                if (hourlyRateTxt.Text == "")
                {
                    throw new Exception("You must enter an hourly rate amount.");
                }
                double hoursWorked = Double.Parse(hoursWorkedTxt.Text);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Exception caught: " + ex.Message);
            }

            try
            {
                if (grossPayTxt.Text == "")
                {
                    throw new Exception("You must enter a gross pay amount.");
                }
                double hoursWorked = Double.Parse(hoursWorkedTxt.Text);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Exception caught: " + ex.Message);
            }

            double salary1 = 10000;
            string name1 = "zak";
            string name2 = "rob";

            double increase1 = salary1 * .04 + salary1;
            double increase2 = increase1 * 1.04;

            Console.WriteLine("Your 2022 salary will be: " + increase2);
            Console.WriteLine("+------------+------------+------------+------------+");
            Console.WriteLine("|    Year    |" + "   " + name1 + "    " + name2 + "   " + salary1.ToString());
        }

        private void clearBtn_Click(object sender, EventArgs e)
        {
            clearAndSetFocus(firstNameTxt);
            clearAndSetFocus(lastNameTxt);
            clearAndSetFocus(departmentTxt);
            clearAndSetFocus(hoursWorkedTxt);
            clearAndSetFocus(hourlyRateTxt);
            clearAndSetFocus(grossPayTxt);
        }

        private void clearAndSetFocus(TextBox input)
        {
            input.Text = "";
            input.Focus();
        }


    }
}
